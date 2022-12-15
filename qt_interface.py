from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog, QMainWindow, QTableWidgetItem, QListWidgetItem
import sys

from db_logic import UsersDB

from config import LIST_WINDOW_UI_PATH, MAIN_WINDOW_UI_PATH, TABLES, DATABASE_PARAMS


class MainWindow(QMainWindow, UsersDB):
    main_window_ui_path = MAIN_WINDOW_UI_PATH

    def __init__(self, db_params):
        super().__init__(db_params=db_params)
        self.db_params = db_params

        # load .ui
        uic.loadUi(self.main_window_ui_path, self)

        self.columns_names = ('surname', 'first_name', 'middle_name', 'street',
                              'house', 'building', 'apartment', 'phone')
        self.headers = (self.header_surname, self.header_first_name, self.header_middle_name, self.header_street,
                        self.header_house, self.header_building, self.header_apartment, self.header_phone)
        self.lists = (self.list_surname, self.list_first_name, self.list_middle_name, self.list_street,
                      self.list_house, self.list_building, self.list_apartment, self.list_phone)
        self.table.setColumnWidth(0, 30)
        self.tables = TABLES
        for i in range(len(self.tables)):
            self.tables[i]['list_widget'] = self.lists[i]

        # connecting widgets to functions
        for header in self.headers:
            header.textChanged[str].connect(self.on_header_changed)
        for list_widget in self.lists:
            list_widget.itemClicked.connect(self.on_list_changed)
        self.button_delete.clicked.connect(self.on_button_delete)
        self.button_search.clicked.connect(self.on_button_search)
        self.button_enter.clicked.connect(self.on_button_enter)
        self.button_update.clicked.connect(self.on_button_update)
        self.button_change_surname.clicked.connect(self.on_button_change)
        self.button_change_first_name.clicked.connect(self.on_button_change)
        self.button_change_middle_name.clicked.connect(self.on_button_change)
        self.button_change_street.clicked.connect(self.on_button_change)
        self.table.itemChanged.connect(self.on_table_changed)

        self.on_button_update()
        self.show()  # show qt interface

    def table_update_all_data(self, data: list = None) -> None:
        """
        Substituting values from the database
        :param data: table values
        :type data: list[iter][str]
        :return: None
        :rtype: None
        """

        all_data = data if data is not None else self.get_all_data()
        self.table.setRowCount(len(all_data))
        if not all_data:
            return self.table.clear()

        for i in range(len(all_data)):
            for j in range(len(all_data[0])):
                item_text = str(all_data[i][j]).strip()
                self.table.setItem(i, j, QTableWidgetItem(item_text))

    def set_list_data(self, table: dict, where_query: dict = None) -> None:
        """
        Set values from database to list widget
        :param table: info about table column
        :type table: dict with keys: 'list_widget', 'value_name', 'table_name'
        :param where_query: filter value
        :type where_query: str
        :return: None
        :rtype: None
        """

        table['list_widget'].clear()
        data = self.get_table_data(table, where_query)
        table['list_widget'].addItems(data)

    @classmethod
    def get_phone_number_converted(cls, phone_number: str) -> str:
        """
        Converting the phone number to the format: +99999999999
        :param phone_number: telephone number
        :type phone_number: str
        :return: converted telephone number
        :rtype: str
        """
        phone_number = phone_number.translate(str.maketrans('', '', '+-()- '))
        if phone_number:
            return f'+{phone_number}'
        return phone_number

    def get_headers_values(self) -> tuple:
        """
        Get values written in headers
        :return: values of headers
        :rtype: tuple
        """
        *data, phone_number = map(lambda x: x.text(), self.headers)
        phone_number = Ui.get_phone_number_converted(phone_number)
        return *data, phone_number

    def on_button_search(self) -> None:
        """
        Callback function when button_search clicked. Updates table with header filter
        :return: None
        :rtype: None
        """
        headers = self.get_headers_values()
        headers_names = map(lambda x: x['value_name'], self.tables)

        to_update = {}
        for value, header_name in zip(headers, headers_names):
            if value:
                to_update[header_name] = value

        data = self.get_all_data(to_update)
        self.table_update_all_data(data)

    def on_button_enter(self) -> None:
        """
        Callback function when button_enter clicked. Adds new values to the database
        :return: None
        :rtype: None
        """
        values = self.get_headers_values()

        if not all(values):
            return QMessageBox.critical(self, "Ошибка ", "Вы заполнили не все поля", QMessageBox.Ok)

        self.add_data(self.tables, *values)
        self.on_button_update()

    def on_button_update(self) -> None:
        """
        Callback function when button_update clicked. Clear values, insert data from the database
        :return: None
        :rtype: None
        """
        self.table_update_all_data()
        for table, header in zip(self.tables, self.headers):
            self.set_list_data(table)
            header.setText('')

    def on_button_delete(self) -> None:
        """
        Callback function when button_delete clicked. Delete row(s)
        :return: None
        :rtype: None
        """
        if not self.table.selectedItems():
            return QMessageBox.critical(self, "Ошибка ", "Вы не выделили удаляемые строки", QMessageBox.Ok)

        selected_items = self.table.selectionModel().selectedRows()
        for selected in selected_items:
            selected_row_id = self.table.itemFromIndex(selected).text()
            self.delete_row('phone_number_baza', 'uniq_id', selected_row_id)

        self.on_button_update()

    def on_button_change(self) -> None:
        """
        Callback function when button_change_* clicked. Open window for editing information
        :return: None
        :rtype: None
        """
        list_window = ListWindow(self.db_params)
        list_window.exec_()

    def on_header_changed(self, text: str) -> None:
        """
        Callback function when the header text changes. Filter values by text in the header
        :param text: header text
        :type text: str
        :return: None
        :rtype: None
        """
        header_name = QApplication.instance().sender().objectName()
        header_name = '_'.join(header_name.split('_')[1:])
        if header_name == 'phone':
            text = MainWindow.get_phone_number_converted(text).replace('+', '')
        table = self.tables[self.columns_names.index(header_name)]
        self.set_list_data(table, {table['value_name']: text})

    def on_list_changed(self, item: QListWidgetItem) -> None:
        """
        Callback function when value is selected from the list. Substitutes the selected value in the header
        :param item: list item
        :type item: QListWidgetItem
        :return: None
        :rtype: None
        """
        list_name = QApplication.instance().sender().objectName()
        list_name = '_'.join(list_name.split('_')[1:])
        header = self.headers[self.columns_names.index(list_name)]
        header.setText(item.text())

    def on_table_changed(self, item: QTableWidgetItem) -> None:
        """
        Callback function when the value of the table has been changed. Update the database
        :param item: table item (table[row][column])
        :type item: QTableWidgetItem
        :return: None
        :rtype: None
        """
        if item.column() == 0:  # check column is not id
            return
        item_text = item.text()
        table = self.tables[item.column() - 1]
        row_id = self.table.item(item.row(), 0).text()
        if item.column() > 4:
            return self.change_list_data('phone_number_baza', table['value_name'], item.text(), 'uniq_id', row_id)
        row_parent_id = self.get_current_data(table['value_id'], table['table_name'], table['value_name'], item_text)
        return self.change_list_data('phone_number_baza', table['table_name'], row_parent_id, 'uniq_id', row_id)


class ListWindow(QDialog, UsersDB):
    list_window_path_ui = LIST_WINDOW_UI_PATH

    def __init__(self, db_params):
        super().__init__(db_params=db_params)

        # load .ui
        uic.loadUi(self.list_window_path_ui, self)
        self.button_name = QApplication.instance().sender().objectName()
        self.button_name = self.button_name.partition('_')[2].partition('_')[2]
        self.set_list_data()

        # connecting widgets to functions
        self.button_list_ok.clicked.connect(self.on_button_list_ok)
        self.button_list_delete.clicked.connect(self.on_button_list_delete)
        self.button_list_apply.clicked.connect(self.on_button_list_apply)

    def set_list_data(self) -> None:
        """
        Setting IDs and Values in a List Widget
        :return: None
        :rtype: None
        """
        all_data = self.get_table_data({'table_name': self.button_name, 'value_name': '*'})
        self.list_table.setRowCount(len(all_data))
        for i in range(len(all_data)):
            for j in range(len(all_data[0])):
                item_text = str(all_data[i][j]).strip()
                self.list_table.setItem(i, j, QTableWidgetItem(item_text))

    def on_button_list_ok(self) -> None:
        """
        Callback function when button_list_ok clicked. Make changes to the database and close the change window
        :return: None
        :rtype: None
        """
        self.on_button_list_apply()
        self.accept()

    def on_button_list_delete(self) -> None:
        """
        Callback function when button_list_delete clicked. Remove value
        :return: None
        :rtype: None
        """
        if not self.list_table.selectedItems():
            return QMessageBox.critical(self, "Ошибка ", "Вы не выделили удаляемые строки", QMessageBox.Ok)

        selected_items = self.list_table.selectionModel().selectedRows()
        for selected in selected_items:
            selected_row_id = self.list_table.itemFromIndex(selected).text()
            self.delete_row('phone_number_baza', self.button_name, selected_row_id)
            self.delete_row(self.button_name, f'{self.button_name}_id', selected_row_id)
        self.set_list_data()

    def on_button_list_apply(self) -> None:
        """
        Callback function when button_list_delete clicked. Save the changes made and update the database
        :return: None
        :rtype: None
        """
        print(self.button_name)
        data_ids = self.get_table_data({'table_name': self.button_name, 'value_name': f"{self.button_name}_id"})
        value_column = 1
        for i in range(self.list_table.rowCount()):
            item = self.list_table.item(i, value_column).text()
            self.change_list_data(self.button_name, f'{self.button_name}_value', item, f'{self.button_name}_id',
                                  data_ids[i])


def main():
    app = QApplication(sys.argv)
    window = MainWindow(DATABASE_PARAMS)
    app.exec_()
    window.close()


if __name__ == '__main__':
    main()
