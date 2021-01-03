from django.shortcuts import render
import json
import requests

def home(request):
    # grab crypto price data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD&api_key={21b14acb429be161ca47749124c4786f38e327c146da7d5f44cb9a9a9e926078}")
    price = json.loads(price_request.content)
    
    #grab Crypto News Data
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key={21b14acb429be161ca47749124c4786f38e327c146da7d5f44cb9a9a9e926078}")
    api = json.loads(api_request.content)
    return render(request, 'home.html',{'api':api,'price':price})  

def prices(request):
    if request.method=="POST":
        quote = request.POST['quote']
        # quote=quote.capitalize()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD&api_key={21b14acb429be161ca47749124c4786f38e327c146da7d5f44cb9a9a9e926078}")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote':quote, 'crypto':crypto})
    else:
        notfound="Enter a crypto currency symbol into the form above..."
        return render(request, 'prices.html', {'notfound':notfound})