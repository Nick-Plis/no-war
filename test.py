import pandas as pd
import json

file = open('file.json')
data = json.load(file)
df_main = pd.DataFrame(data)

file = open('text.txt', 'w')
file.write(df_main.to_string())