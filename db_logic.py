import psycopg2


class UsersDB:
    def __init__(self, db_params):
        dbname, user, password = db_params['name'], db_params['user'], db_params['password']
        host, port = db_params['host'], db_params['port']
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """SELECT setval('phone_number_baza_uniq_id_seq', (SELECT max(uniq_id) FROM public.phone_number_baza))""")

    @classmethod
    def get_where_query(cls, where_query_variables: dict) -> str:
        """
        Forms part of the query with WHERE
        :param where_query_variables: dict with keys 'value_name', 'value'
        :type where_query_variables: dict
        :return: Query line
        :rtype: str
        """
        query = "\nWHERE "
        for value_name, value in where_query_variables.items():
            query += f"{value_name} LIKE ('%{value}%')"
            query += " AND "
        query = query[:-5]
        return query

    def get_all_data(self, where_query_variables: dict = None) -> list:
        """
        Getting all data from the main table
        :param where_query_variables: dict with keys 'value_name', 'value'
        :type where_query_variables: dict
        :return: all data list
        :rtype: list
        """
        query = '''
            SELECT uniq_id, surname_value, first_name_value, middle_name_value, street_value,
             house, building, apartment, phone_number 
            FROM phone_number_baza
            JOIN surname ON phone_number_baza.surname = surname.surname_id
            JOIN first_name ON phone_number_baza.first_name = first_name.first_name_id
            JOIN middle_name ON phone_number_baza.middle_name = middle_name.middle_name_id
            JOIN street ON phone_number_baza.street = street.street_id
        '''

        if where_query_variables:
            where_query = self.get_where_query(where_query_variables)
            query += where_query

        query += '\nORDER BY uniq_id'
        self.cur.execute(query)

        data = self.cur.fetchall()
        data = list(map(lambda x: tuple(map(lambda y: str(y).strip(), x)), data))
        return data

    def get_table_data(self, variables, where_query_variables: dict = None) -> list:
        """
        Getting data from a table
        :param variables: Values that form the query
        :type variables: dict with keys: 'value_id'; 'table_name'; 'value_name'; 'enter_value'
        :param where_query_variables: dict with keys 'value_name'; 'value'
        :type where_query_variables: dict
        :return: [] | Sorted list of values
        :rtype: list
        """
        query_template = '''SELECT DISTINCT {value_name} FROM {table_name} '''
        query = self.build_query(variables, query_template)

        if where_query_variables:
            where_query = self.get_where_query(where_query_variables)
            query += where_query
        self.cur.execute(query)
        data = self.cur.fetchall()

        if variables['value_name'] == '*':
            return sorted(data, key=lambda x: x[0])

        data = [str(x[0]).strip() for x in data]

        # sorting mixed values (with letters and numbers)
        if any(map(lambda x: x.isdigit(), data)):
            return sorted(data, key=lambda x: int('0' + ''.join(filter(str.isdigit, x))))
        return sorted(data)

    def add_data(self, tables_info: dict,
                 surname: str, first_name: str, middle_name: str, street: str, *other_values: list[str]) -> None:
        """
        Adding data to a table
        :param tables_info: dict with keys: 'value_id'; 'table_name'; 'value_name'; 'enter_value'
        :type tables_info: dict
        :param surname: Column surname
        :type surname: str
        :param first_name: Column first_name
        :type first_name: str
        :param middle_name:
        :type middle_name:
        :param street: Column street
        :type street: str
        :param other_values: Other columns: house, building, apartment, phone_number
        :type other_values: list[str]
        :return: None
        :rtype: None
        """
        query_template_select = '''SELECT {value_id} FROM public.{table_name} WHERE {value_name} = '{enter_value}' '''
        query_template_insert = '''INSERT INTO public.{table_name} ({value_name})
                                   VALUES ('{enter_value}') RETURNING {value_id}'''

        values_ids = []

        for table, enter_value in zip(tables_info[:4], (surname, first_name, middle_name, street)):
            table['enter_value'] = enter_value
            query = self.build_query(table, query_template_select)
            self.cur.execute(query)
            response = self.cur.fetchone()

            if response:
                values_ids.append(response[0])
                continue

            query = self.build_query(table, query_template_insert)
            self.cur.execute(query)
            values_ids.append(self.cur.fetchone()[0])

        self.cur.execute('''
               INSERT INTO public.phone_number_baza (
               surname, first_name, middle_name, street, house, building, apartment, phone_number
               )
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',
                         (*values_ids, *other_values))

        self.conn.commit()

    def delete_row(self, table_name: str, column_name: str, row_id: str) -> None:
        """
        Removing row from the database
        :param table_name: Name of the table
        :type table_name: str
        :param column_name: Column heading to be removed to be deleted
        :type column_name: str
        :param row_id: ID of the column to be deleted
        :type row_id: str
        :return: None
        :rtype: None
        """
        self.cur.execute(f'''DELETE FROM {table_name}
                            WHERE {column_name} = '{row_id}' ''')
        self.conn.commit()

    def get_current_data(self, value_id: str, table_name: str, value_name: str, new_data: str):
        """
        Modifies the data, creates new reference to the value if necessary
        :param value_id: Value ID
        :type value_id: str
        :param table_name: Table title where the data comes from
        :type table_name: str
        :param value_name: Value name
        :type value_name: str
        :param new_data: new value of param
        :type new_data: str
        :return: Value ID
        :rtype: str
        """
        query_select = f'''SELECT {value_id} FROM {table_name}
                            WHERE {value_name} = '{new_data}' '''
        query_insert = f'''INSERT INTO public.{table_name} ({value_name}) 
                            VALUES ('{new_data}') RETURNING {value_id}'''

        self.cur.execute(query_select)
        response = self.cur.fetchone()
        if not response:
            self.cur.execute(query_insert)
            response = self.cur.fetchone()

        row_parent_id = response[0]
        return row_parent_id

    def change_list_data(self, table_name: str, value_name: str, item_value: str, value_id: str, row_id: str) -> None:
        """
        Update database value
        :param table_name: Table title where the data comes from
        :type table_name: str
        :param value_name: Value name
        :type value_name: str
        :param item_value: Value
        :type item_value: str
        :param value_id: Value ID
        :type value_id: str
        :param row_id: Row ID
        :type row_id: str
        :return: None
        :rtype: None
        """
        self.cur.execute(
            f'''UPDATE {table_name} SET {value_name} = '{item_value}' WHERE {value_id} = '{row_id}' ''')
        self.conn.commit()

    @staticmethod
    def build_query(variables: dict, base_sql_query: str) -> str:
        """
        Form a query for the database
        :param variables: Dictionary of values that are substituted into the template query
        :type variables: dict
        :param base_sql_query: Query template
        :type base_sql_query: str
        :return: Formed query
        :rtype: str
        """
        return base_sql_query.format(**variables)

    def close(self):
        """Closing the database"""
        self.cur.close()
        self.conn.close()

    def __del__(self):
        self.close()


def main():
    pass
    # test = UsersDB(DATABASE_PARAMS)


if __name__ == '__main__':
    main()
