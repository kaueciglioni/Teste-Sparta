# Teste para o processo seletivo da Sparta Investimentos
Nesse projeto, de maneira básica e com o aprendizado acadêmico foi criado 3 scripts para rodar de forma respectivas, onde criamos o banco de dados com a planilha fornecida, importação do dados para o banco de dados, e por útlimo uma query para realizar a consulta das informações além de alguns inputs para facilidade no entedimentos da informações consultadas.

Apenas de biblioteca usamos o , PANDAS, REQUEST, SQLITE, por facilidade no manuseio e trabalhar na linguagem SQL, onde ele no próprio VSC cria um banco de dados com todos os dados importados, e traz pra você um representação de tabela.
Dificuldade apenas com o nivel de complexidade do uso de banco de dados, onde temos que ter todo o cuidado para a configuração do banco de dados, onde através do pandas é puxada todas as informações solicitadas no processo.

Foram adicionadas informações a mais para que possa ter um melhor entendimento, e também para a informação mais próxima da completa no banco de dados.


## Sistema de Consulta de Companhias Abertas

Este sistema em Python permite persistir informações sobre companhias abertas em um banco de dados SQLite e consultar essas informações posteriormente. Ele consiste em três scripts:

### import_data.py

Este script importa os dados do arquivo CSV fornecido pelo usuário para o banco de dados SQLite.

### query_data.py

Este script permite consultar as informações das companhias armazenadas no banco de dados SQLite. Ele solicitará que o usuário insira o CNPJ da empresa e, opcionalmente, uma data específica para consultar informações em datas passadas.

### create_database.py

Este script cria o banco de dados SQLite e a tabela necessária para armazenar as informações das companhias.

# Utilização 

1. **Instalação**: Clone este repositório.

2. **Criar o Banco de Dados**: Execute `python create_database.py`.

3. **Importar Dados**: Importe os dados do arquivo CSV para o banco de dados com `python import_data.py caminho/do/seu/arquivo.csv`.

4. **Consultar Informações**: Execute `python query_data.py` e siga as instruções no terminal para consultar as informações das companhias.

O banco de dados possui a seguinte estrutura:
- Tabela `companhia`: `id` (chave primária), `cnpj_cia`, `denom_social`, `sit`, `data`.

