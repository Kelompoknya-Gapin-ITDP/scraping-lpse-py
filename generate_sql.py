import json

sql_statements = []
table_name = "tender_data"

json_data = []
with open('result.json', 'r') as file:
    json_data = json.load(file)

def format_value(value):
    if isinstance(value, str):
        return f"'{value.replace("'", "''")}'"  
    elif value is None:
        return 'NULL'
    else:
        return str(value)

sql_statements = []
table_name = "tender_data"

for item in json_data:
    columns = ', '.join(item.keys())
    values = ', '.join([format_value(value) for value in item.values()])
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
    sql_statements.append(sql)

sql_statements_str = ','.join(str(x) for x in sql_statements)

with open('result.sql', 'w') as file:
    file.write(sql_statements_str)