import requests
import json

from django.shortcuts import render


def home(request):
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD,EUR")
    price = json.loads(price_request.content)
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    primary = 'primary'
    success = 'success'
    warning = 'warning'
    danger = 'danger'
    info = 'info'
    context = {
        'api': api,
        'price': price,
        'primary': primary,
        'success': success,
        'warning': warning,
        'danger': danger,
        'info': info
    }
    return render(request, 'home.html', context=context)


def prices(request):
    if request.method == "POST":
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD,EUR")
        crypto = json.loads(crypto_request.content)
        primary = 'primary'
        success = 'success'
        warning = 'warning'
        danger = 'danger'
        info = 'info'
        context = {
            'quote': quote,
            'crypto': crypto,
            'primary': primary,
            'success': success,
            'warning': warning,
            'danger': danger,
            'info': info
        }
        return render(request, 'prices.html', context=context)

    else:
        return render(request, 'prices.html', {})
