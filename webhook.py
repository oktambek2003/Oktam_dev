import requests

url = "https://oktambek.pythonanywhere.com/home"

TOKEN = "6063934394:AAExwcUz_3z3LICpws1dzUfZjqN7KtOLbMk"
payload = {
    "url": url
}

response = requests.get(f'https://api.telegram.org/bot{TOKEN}/setWebhook', params=payload)
print(response.status_code)