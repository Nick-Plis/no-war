import pandas as pd
import pyodbc
import json
import os.path

def json_check():
    file = open('file.json')
    data = json.load(file)
    df_main = pd.DataFrame(data)
    return df_main


df_codewords = pd.read_csv('rb_codewords.csv')

while True:
    try:
        df_main = json_check()
        if  df_codewords['codeword'].isin(df_main['codeword']):
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

        df_main.to_csv(r'main_requests.csv', mode='a', header=False)

    except:
        continue

