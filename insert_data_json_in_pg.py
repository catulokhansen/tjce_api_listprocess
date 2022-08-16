from genericpath import isfile
from msilib.schema import tables
from sqlite3 import Timestamp
from venv import create
from datetime import datetime
import time
import psycopg2, json, csv, os

# Connect database postresql
con = psycopg2.connect(dbname="dev_project", user="postgres", password="12345678", host="localhost")
cur = con.cursor()

# Sql postgresql - insert
insert_sql = """INSERT INTO tj_process.tj_process (
            id,
            numero, 
            numero_formatado, 
            data_protocolo,
            data_primeira_dist, 
            localizacao,
            ultima_mov_desc,
            data_ultima_mov,
            ultima_mov_desc_com,
            situacao,
            date_record                    
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# List directory on files jsons
dir_path = 'jsons'
res = os.listdir(dir_path)

# Loop to get the json files returned by API and write to the database
for row in res:
 
 # Variable with the path of the returned json files 
 dir_path = 'jsons/' + row

 # Open the returned jsons files
 with open(dir_path, 'r', encoding='utf-8') as file:
        
        # Variable to store the sealized json
        read_json = json.load(file)
        date_record = datetime.now()
                      
        # Loop to iterate over the content in the json and insert the data into the database
        for record in read_json:
          cur.execute(insert_sql, (record['id'], record['numero'], record['numeroFormatado'], record['dataProtocolo'], 
          record['dataPrimeiraDistribuicao'], record['localizacao'], 
          record['ultimaMovimentacao']['descricao'],record['ultimaMovimentacao']['data'], 
          record['ultimaMovimentacao']['complemento'], record['situacao'], date_record))
        con.commit()


     
        


    
        



