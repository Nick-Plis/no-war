import pandas as pd
import pyodbc
import json

file = open('file.json')
data = json.load(file)
df_main = pd.DataFrame(data)

main_requests = pyodbc.connect('Driver={SQL Server};Server=localhost\SQLEXPRESS;Database=master;Trusted_Connection=True;')
rb_codewords = pyodbc.connect('Driver={SQL Server};Server=localhost\SQLEXPRESS;Database=master;Trusted_Connection=True;')
cursor_main = main_requests.cursor()

df_codewords = pd.read_sql('rb_codewords', rb_codewords)
if df_main['codeword'] in df_codewords['codeword']:
    df_main['request_time'] = pd.to_datetime(df_main['request_time'])
    df_codewords['date_to'] = pd.to_datetime(df_codewords['date_to'])
    if df_main['request_time'] < df_codewords['date_to']:
        pass

    else:
        df_main = pd.DataFrame(df_main['id', 'request_ip', 'request_time',
                                       'district_id', 'where', 'when', 'importance_id',
                                       'request', 'phone', 'name'], columns=df_main.columns)

else:
    df_main = pd.DataFrame(df_main['id', 'request_ip', 'request_time',
                                   'district_id', 'where', 'when', 'importance_id',
                                   'request', 'phone', 'name'], columns=df_main.columns)

for row in df_main.itertuples():
    cursor_main.execute(
        " INSERT INTO main_requests(id, request_ip, request_time, district_id, where, when, importance_id, codeword, request, phone, name)VALUES (?,?,?,?,?,?,?,?,?,?)",
        row.id,
        row.request_ip,
        row.request_time,
        row.district_id,
        row.where,
        row.when,
        row.importance_id,
        row.codeword,
        row.request,
        row.phone,
        row.name
    )
main_requests.commit()