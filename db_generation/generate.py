import psycopg2
import random


def build_query(variables: dict, base_sql_query: str) -> str:
    return base_sql_query.format(**variables)


def print_all_data(conn):
    cur = conn.cursor()

    cur.execute(f'''SELECT uniq_id, surname_value, first_name_value, middle_name_value, street_value, house, building, apartment, phone_number FROM phone_number_baza
                JOIN surname ON phone_number_baza.surname = surname.surname_id
                JOIN first_name ON phone_number_baza.first_name = first_name.first_name_id
                JOIN middle_name ON phone_number_baza.middle_name = middle_name.middle_name_id
                JOIN street ON phone_number_baza.street = street.street_id''')
    rows = cur.fetchall()

    for row in rows:
        print("uniq_id = ", row[0])
        print("fam = ", row[1])
        print("name = ", row[2])
        print("othc = ", row[3])
        print("street = ", row[4])
        print("building = ", row[5])
        print("kor = ", row[6])
        print("appartments = ", row[7])
        print("tel = ", row[8])
        print('')
    print("Operation done successfully")
    cur.close()


def insert_values(conn, data: dict):
    cur = conn.cursor()
    tel_baza_sql_query = '''INSERT INTO public.phone_number_baza (uniq_id, surname, first_name, middle_name, street, house, building, apartment, phone_number)
         VALUES ('{uniq_id}', '{fam}', '{name}', '{otch}', '{street}', '{building}', '{kor}', '{appartments}', '{tel}')'''
    cur.execute(build_query(data, tel_baza_sql_query))
    cur.close()
    conn.commit()


def table_generate_data(conn):
    rows_number = 50
    random_a, random_b = 1, 9
    random_building_a, random_building_b = 1, 30
    random_kor_a, random_kor_b = 1, 5
    random_apartment_a, random_apartment_b = 1, 500

    for i in range(rows_number):
        a = i + 1
        data_base = {'uniq_id': a,
            'fam': random.randint(random_a, random_b),
            'name': random.randint(random_a, random_b),
            'otch': random.randint(random_a, random_b),
            'street': random.randint(random_a, random_b),
            'building': random.randint(random_building_a, random_building_b),
            'kor': random.randint(random_kor_a, random_kor_b),
            'appartments': random.randint(random_apartment_a, random_apartment_b),
            'tel': f'+7{random.randint(1000000000, 9999999999)}',
        }
        insert_values(conn, data_base)


def main():
    conn = psycopg2.connect(database="DB_PHONE_NUMBERS",
                            user="postgres",
                            password="YOUR PASSWORD",
                            host="127.0.0.1",
                            port="5432")
    print('Opened database successfully')
    table_generate_data(conn)
    print_all_data(conn)

    conn.close()


if __name__ == '__main__':
    main()
