import requests
import json

def get_crypto_data(ticker):
    url = f"https://api.coinmarketcap.com/v1/ticker/{ticker}/?convert=USD"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def send_message(chat_id, message):
    url = f"https://api.telegram.org/bot<1788261935:AAFhC8FQCGJBxZV7uWZmfPcvHpKzQtfqPLc>/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)

def main():
    ticker = "bitcoin"
    data = get_crypto_data(ticker)
    message = f"{ticker} price: ${data[0]['price_usd']}"
    chat_id = "<CHAT_ID>"
    send_message(chat_id, message)

if __name__ == "__main__":
    main()
