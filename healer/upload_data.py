import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
import re

from sqlalchemy.sql.expression import table


def name_striper(file_path):
    stripped=file_path.split('/')
    file_name=re.sub('.csv','',stripped[-1])
    table_name=file_name.lower()
    return table_name
    

def read_csv(file_path):
    print("reading CSV file")
    table_name=name_striper(file_path)
    if table_name=='addrc':
       addresses = pd.read_csv(file_path, names=['period','practice_code','practice_name','health_centre','street','city','country','post_code'],dtype=str)
       return addresses, table_name 
    if table_name=='chemc':
       chemicals = pd.read_csv(file_path, names=['chem_sub','name','period'],dtype=str)
       return chemicals, table_name
    if table_name=='pdpic':
       practices = pd.read_csv(file_path, names=['sha','pct','practice','bnf_code','bnf_name','items','nic','act_cost','quantity','period'],dtype=str)
       return practices, table_name



    
def upload_to_db(file, table_name):
    print("Connecting to DB")
    engine = create_engine('postgresql://developer:secret@localhost:5432/postgres')
    with engine.connect() as connection:
        # connection.execute(text("DROP TABLE pdpic"))
        connection.execute(text("DROP TABLE addrc"))
        # connection.execute(text("DROP TABLE chemc"))
        print("Loading data to db")
        file.to_sql(table_name, engine)
    return "Table Sucessfully Created"    
        
        
def upload_data(file_path):
    file,table_name=read_csv(file_path)
    upload_to_db(file, table_name)
    return "Uploading file to DB"

    

