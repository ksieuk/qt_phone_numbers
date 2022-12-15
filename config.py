import os


MAIN_WINDOW_UI_PATH = 'static/main_window.ui'
LIST_WINDOW_UI_PATH = 'static/list_window.ui'

DATABASE_PARAMS = {
    'name': "DB_PHONE_NUMBERS",
    'user': "postgres",
    'password': os.getenv('PASSWORD') or 'YOUR PASSWORD HERE',
    'host': "127.0.0.1",
    'port': "5432",
}

TABLES = [
        {'table_name': 'surname',
         'value_name': 'surname_value',
         'value_id': 'surname_id'},

        {'table_name': 'first_name',
         'value_name': 'first_name_value',
         'value_id': 'first_name_id'},

        {'table_name': 'middle_name',
         'value_name': 'middle_name_value',
         'value_id': 'middle_name_id'},

        {'table_name': 'street',
         'value_name': 'street_value',
         'value_id': 'street_id'},

        {'table_name': 'phone_number_baza',
         'value_name': 'house'},

        {'table_name': 'phone_number_baza',
         'value_name': 'building'},

        {'table_name': 'phone_number_baza',
         'value_name': 'apartment'},

        {'table_name': 'phone_number_baza',
         'value_name': 'phone_number'},
]
