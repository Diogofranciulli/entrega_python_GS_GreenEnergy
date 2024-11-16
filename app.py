import requests
import time

# Configurações da API do Thingspeak
CHANNEL_ID = '2738000'
READ_API_KEY = 'N9COWLMH4HO63N2U'
BASE_URL = f'https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json'


# Função para obter dados do Thingspeak
def get_thingspeak_data():
    params = {
        'api_key': READ_API_KEY,
        'results': 1
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data['feeds'][0]  # Retorna o último feed
    except requests.RequestException as e:
        print("Erro ao acessar a API do Thingspeak:", e)
        return None


# Função para processar os dados do Thingspeak e exibir no console
def process_data(feed):
    if feed:
        latitude = feed.get('field1', 'N/A')
        longitude = feed.get('field2', 'N/A')
        pais = feed.get('field3', 'N/A')
        cidade = feed.get('field4', 'N/A')
        temperatura_reservatorio_1 = feed.get('field5', 'N/A')
        temperatura_reservatorio_2 = feed.get('field6', 'N/A')
        tensao_gerador = feed.get('field7', 'N/A')

        data_string = (
            f"Latitude: {latitude}\n"
            f"Longitude: {longitude}\n"
            f"País: {pais}\n"
            f"Cidade: {cidade}\n"
            f"Temperatura do Reservatório Água Fria: {temperatura_reservatorio_1} °C\n"
            f"Temperatura do Reservatório Água Quente: {temperatura_reservatorio_2} °C\n"
            f"Tensão do Gerador: {tensao_gerador} V\n"
        )
        print("Dados do Thingspeak:\n", data_string)

        # Salva os dados em um arquivo
        save_data_to_file(data_string)

        # Retorna os dados em formato de lista para manipulação futura
        return [
            latitude, longitude, pais, cidade,
            temperatura_reservatorio_1, temperatura_reservatorio_2,
            tensao_gerador
        ]
    else:
        print("Feed vazio.")
        return []


# Função para salvar os dados em um arquivo
def save_data_to_file(data_string):
    try:
        with open('dados_solar.txt', 'a') as file:
            file.write(data_string + "\n" + "-" * 30 + "\n")
    except IOError as e:
        print("Erro ao salvar dados no arquivo:", e)


# Função principal para obter e processar os dados periodicamente
def main():
    UPDATE_INTERVAL = 10
    registros = []

    while True:
        feed = get_thingspeak_data()
        dados = process_data(feed)

        if dados:
            registros.append(dados)
            cidades = [dado[3] for dado in registros if dado[3] != 'N/A']
            print(f"Cidades registradas até agora: {', '.join(cidades)}")

        # Espera antes de realizar a próxima atualização
        time.sleep(UPDATE_INTERVAL)



if __name__ == "__main__":
    main()
