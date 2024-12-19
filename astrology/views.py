from django.shortcuts import render
from .utils import fetch_daily_horoscope

def home(request):
    return render(request, 'astrology/home.html')

def horoscope(request):
    prediction = None
    if request.method == 'POST':
        sign = request.POST.get('sign')
        prediction = fetch_daily_horoscope(sign)
    return render(request, 'astrology/horoscope.html', {'prediction': prediction})
