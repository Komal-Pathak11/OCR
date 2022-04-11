from django.shortcuts import render, redirect
from googletrans import Translator

# Create your views here.

def home(request):
    return render(request, "index.html")

def translated(request):
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    translator = Translator()
    dt = translator.detect(text)
    dt2 = dt.lang
    translated =translator.translate(text, lang)
    tr = translated.text
    return render(request, 'translated.html', {'translated': tr})


