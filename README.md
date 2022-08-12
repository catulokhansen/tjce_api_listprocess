The purpose of these script is to consult the status of the process in the ESAJ system of the TJCE

NOTE: File numbers_process.csv
This file must store the list of processes to be consulted.
# Script execution sequence

1 . First step - Run script get_token.py to get the token for authentication on the API:
    *Description
    URl to get token for use in requests to the service "numeroProccesoParteProcesso" 
    REST request 
    POST => https://consultaprocesso.tjce.jus.br/scpu-web/api/kdjklsajdls/jsldaskd
    Parameter
    {
    "nomeUsuario": "",
    "senha": ""
    }
    
    NOTE 1: The token will be saved in the file "token.txt"
    NOTE 2: Token expires in 30 seconds


2. Second step - Run script post_request_api_tj.py to query the TJCE REST AP, and the return record in the jsons directory
    *Description
    URl API to for requests to the service "numeroProccesoParteProcesso" 
    REST request 
    POST => https://consultaprocesso.tjce.jus.br/scpu-web/api/consulta/numeroProcessoParteProcesso/
    Parameters
    {
        "numeroProcesso" : "",
        "nomeParte" : "",
        "cpf_cnpj" : "",
        "rg" : "",
        "nomeMae" : "",
        "nomePai" : "",
        "idClasse": "",
        "descricaoClasse": ""
    }

    NOTE 1: The parameter that the script is passing in the POST is "numeroProcesso", to pass another one is modify the line below the comment "# Parameters sen API"
    NOTE 2: 

3. Third step - Run script insert_data_json_in_pg.py to record in database the jsons files (stored in direcotry /jsons) returned by the API
    NOTE 1: Modify the database connection string in the "con" variable 











