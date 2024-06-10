import pandas as pd
import sqlite3
import sys

def import_company_data(csv_file):
    try:
        df = pd.read_csv(csv_file, sep=';', usecols=['CNPJ_CIA', 'DENOM_SOCIAL', 'SIT', 'DT_CANCEL', 'DT_INI_SIT'])
        df['DT_CANCEL'] = pd.to_datetime(df['DT_CANCEL'], errors='coerce')
        df['DT_INI_SIT'] = pd.to_datetime(df['DT_INI_SIT'], errors='coerce')

        conexaodb = sqlite3.connect('companhias.db')
        df.to_sql('companhia', conexaodb, if_exists='replace', index=False)
        conexaodb.close()

        print("Dados importados com sucesso para o banco de dados.")
    except Exception as e:
        print("Erro ao importar dados:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Por favor, forneça o caminho para o arquivo CSV.")
        sys.exit(1)

    csv_file = sys.argv[1]
    import_company_data(csv_file)
