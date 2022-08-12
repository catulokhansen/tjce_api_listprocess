from distutils.file_util import write_file
import requests, csv, json, codecs
from get_token import token


# Read number proccess in tj_processos_arquivados
with open('numbers_processos.csv','r') as file:
    number = csv.reader(file)
    
    # Iterate lines on cvs
    for row in number:
        #URL API TJ-Ce
        url = 'https://consultaprocesso.tjce.jus.br/scpu-web/api/consulta/numeroProcessoParteProcesso/'
        
        # Parameters send API
        processo_data = {
             "numeroProcesso": row[0]
        }
       
        #Token send authentication
        headers = {
            'Authorization': token
        }

        # Send verb HTTP POST with parameters
        response = requests.post(url=url, json=processo_data, headers=headers)

        # Write API return in json in directory JSONS
        if response.status_code >= 200 and response.status_code <= 299:
            with open(r"jsons/""tj_" + str(row[0]) + ".json", 'w', encoding='utf-8') as result:
                data = response.text
                result.write(data)
                
       



   

