# Projeto: Coleta de Dados de Energia Solar com Thingspeak

**Diogo Leles Franciulli - RM: 558487** <br>
**Felipe Sousa De Oliveira - RM: 559085** <br>
**Ryan Brito Pereira Ramos - RM: 554497** <br>

Este projeto em Python utiliza a API do **Thingspeak** para coletar e processar dados relacionados a um sistema de energia solar. Os dados incluem localização, informações sobre os reservatórios de água (temperatura) e a tensão do gerador de energia. As informações são exibidas no console, salvas em um arquivo e registradas em tempo real.

---

## **Descrição Geral**

O código acessa a API do Thingspeak para obter o feed mais recente de dados publicados no canal configurado. Ele processa esses dados, exibe no console e salva em um arquivo de texto para análise futura. Além disso, mantém um histórico das cidades registradas.

---

## **Funcionalidades**

1. **Obtenção de Dados do Thingspeak**:
   - Faz requisições para a API do Thingspeak usando a biblioteca `requests`.
   - Recupera o feed mais recente do canal configurado.

2. **Processamento de Dados**:
   - Extrai informações como latitude, longitude, país, cidade, temperaturas dos reservatórios e tensão do gerador.
   - Exibe os dados processados no console.

3. **Armazenamento de Dados**:
   - Salva os dados coletados em um arquivo de texto chamado `dados_solar.txt`.

4. **Monitoramento Contínuo**:
   - Atualiza os dados em um intervalo configurável (10 segundos por padrão).
   - Mantém um registro das cidades registradas em tempo real.

---

## **Como Usar**

1. **Pré-requisitos**:
   - Python 3.x instalado.
   - Biblioteca `requests` instalada:
     ```bash
     pip install requests
     ```

2. **Configuração**:
   - Substitua os valores das variáveis `CHANNEL_ID` e `READ_API_KEY` com os dados do seu canal no Thingspeak.

3. **Execução**:
   - Execute o script no terminal:
     ```bash
     python nome_do_arquivo.py
     ```

---

## **Estrutura do Código**

### **1. Importação de Bibliotecas**
```python
import requests
import time
```
- `requests`: Para realizar requisições HTTP à API do Thingspeak.
- `time`: Para controlar o intervalo entre as requisições.

---

### **2. Configuração da API**
```python
CHANNEL_ID = '2738000'
READ_API_KEY = 'N9COWLMH4HO63N2U'
BASE_URL = f'https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json'
```
- **`CHANNEL_ID`**: ID do canal no Thingspeak.
- **`READ_API_KEY`**: Chave de leitura da API do canal.
- **`BASE_URL`**: URL base para acessar os dados do canal.

---

### **3. Função para Obter Dados do Thingspeak**
```python
def get_thingspeak_data():
    ...
```
- Faz uma requisição GET à API e retorna o último feed do canal.
- Trata erros de conexão e retorna `None` em caso de falha.

---

### **4. Função para Processar Dados**
```python
def process_data(feed):
    ...
```
- Extrai as informações relevantes do feed.
- Exibe os dados formatados no console.
- Chama a função `save_data_to_file` para salvar os dados.

---

### **5. Função para Salvar Dados em Arquivo**
```python
def save_data_to_file(data_string):
    ...
```
- Salva os dados formatados no arquivo `dados_solar.txt`.
- Adiciona separadores para facilitar a leitura.

---

### **6. Função Principal**
```python
def main():
    ...
```
- Executa a coleta e processamento de dados em um loop infinito.
- Atualiza os dados a cada intervalo configurado (10 segundos).
- Mantém um histórico de cidades registradas.

---

## **Exemplo de Saída**

No console:
```
Dados do Thingspeak:
Latitude: -23.5505
Longitude: -46.6333
País: Brasil
Cidade: São Paulo
Temperatura do Reservatório Água Fria: 25 °C
Temperatura do Reservatório Água Quente: 60 °C
Tensão do Gerador: 12.5 V

Cidades registradas até agora: São Paulo
```

No arquivo `dados_solar.txt`:
```
Latitude: -23.5505
Longitude: -46.6333
País: Brasil
Cidade: São Paulo
Temperatura do Reservatório Água Fria: 25 °C
Temperatura do Reservatório Água Quente: 60 °C
Tensão do Gerador: 12.5 V
------------------------------
```

---

## **Melhorias Futuras**

- Adicionar interface gráfica para exibir os dados.
- Implementar alertas para valores críticos, como alta tensão ou temperaturas extremas.
- Permitir configuração do intervalo de atualização via interface.

---

## **Dependências**

- Python 3.x
- Biblioteca `requests`

---

## **Licença**

Este projeto está sob a licença **MIT**. Sinta-se à vontade para usá-lo, modificá-lo e distribuí-lo.

---