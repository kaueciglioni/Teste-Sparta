import sqlite3

def query_company_data(cnpj, query_date=None):
    cnpj = ''.join(filter(str.isdigit, cnpj))
    cnpj = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
    
    conexaodb = sqlite3.connect('companhias.db')
    cursor = conexaodb.cursor()

    try:
        if query_date:
            cursor.execute('''
            SELECT * FROM companhia
            WHERE cnpj_cia = ? AND DATE(data) <= ?
            ORDER BY DATE(data) DESC LIMIT 1
            ''', (cnpj, query_date))
        else:
            cursor.execute('''
            SELECT * FROM companhia
            WHERE cnpj_cia = ?
            ORDER BY DATE(data) DESC LIMIT 1
            ''', (cnpj,))

        result = cursor.fetchone()
    except Exception as e:
        print("Erro na consulta:", e)
        result = None

    conexaodb.close()
    return result

def get_cnpj_input():
    while True:
        cnpj = input("Por favor, insira o CNPJ da empresa (apenas números): ")
        if len(cnpj) == 14 and cnpj.isdigit():
            return cnpj
        else:
            print("O CNPJ deve conter 14 números.")

def main():
    cnpj = get_cnpj_input()
    query_date = input("Deseja consultar uma data específica? (formato: YYYY-MM-DD) [Deixe em branco para consultar a data mais recente]: ")
    data = query_company_data(cnpj, query_date)
    if data:
        print("Informações da empresa:")
        print("CNPJ:", data[1])
        print("Denominação Social:", data[2])
        print("Situação:", data[3])
        print("Data da última atualização:", data[4])
    else:
        print("Nenhuma informação encontrada para o CNPJ fornecido.")

if __name__ == "__main__":
    main()
