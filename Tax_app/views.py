from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
Tax_rate = 0.15

def Tax_page(request):
    return render(request , "Tax_app/tax_01.html")

def calculate_price(request , price):
    price = float(price + (price * Tax_rate))
    return render( request, "Tax_app/total_price_02.html",{"p": price})

def Tax_value(request):

    return render(request , "Tax_app/Tax_rate_03.html", {"Tax": Tax_rate * 100 })
