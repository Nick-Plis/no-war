import pandas as pd
import json
import os.path


try:
    df_codewords = pd.read_csv('rb_codewords.csv')
    file = open('file.json')
    data = json.load(file)
    df_main = pd.DataFrame(data)
    if df_codewords['codeword'].isin(df_main['codeword']):
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

except:
    pass

print('123')
df_main.to_csv(r'main_requests.csv', header=False, index=False)
