import pandas, sys
uri_excel_path=sys.argv[1]
sys.stdout.reconfigure(encoding='utf-8')
excel_data_df = pandas.read_excel(uri_excel_path, sheet_name='data')
json_str = excel_data_df.to_json(orient='records')
print(json_str)