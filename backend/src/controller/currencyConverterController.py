import tkinter as tk
from tkinter import Label, Entry, END, Button
import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = f'https://open.er-api.com/v6/latest/'

    def convert(self, from_currency, to_currency, amount):
        try:
            response = requests.get(self.url + from_currency)
            data = response.json()

            if data['result'] == 'success':
                rate = data['rates'][to_currency]
                return amount * rate
            else:
                raise Exception("API request failed")
        except Exception as e:
            return f"Error: {e}"

    def get_supported_currencies(self):
        try:
            response = requests.get(self.url + 'USD')
            data = response.json()
            if data['result'] == 'success':
                return list(data['rates'].keys())
            else:
                raise Exception("API request failed")
        except Exception as e:
            return f"Error: {e}"

converter = CurrencyConverter('your_api_key')

if __name__ == "__main__":
    amount = float(1000000)

    result = converter.convert('COP', 'CHF', amount)
    print(f"Converted value : {result}")
