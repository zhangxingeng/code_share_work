from IPython.core.getipython import get_ipython
import pandas as pd

def create_new_cell(contents):
    shell = get_ipython()
    payload = dict(
        source='set_next_input',
        text=contents,
        replace=False,
    )
    shell.payload_manager.write_payload(payload, single=False)

def get_df(file_name, df_name):
    content = "{df} = pd.read_csv('{file}', names=['Name', 'Age', 'Height'])\n"\
               "{df}.sort_values(by='Age', inplace=True)\n"\
               "{df}"\
               .format(df=df_name, file=file_name)
    create_new_cell(content)

file_list = ['filename_1.csv', 'filename_2.csv']
name_list = ['df1', 'df2']
for file, name in zip(file_list, name_list):
    get_df(file, name)
