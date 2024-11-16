from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.staticfiles import finders
import os
from django.http import HttpResponse

def home(request):
    bg_dir = os.path.join('static', 'BG')
    BG_list = [f'BG/{f}' for f in os.listdir(bg_dir) if f.endswith(('.png',))]  # Prepend 'BG/' to each filename

    hands_dir = os.path.join('static', 'Hands')
    Hands_list = [f'Hands/{f}' for f in os.listdir(hands_dir) if f.endswith(('.png',))]  # Prepend 'BG/' to each filename

    outfits_dir = os.path.join('static', 'OUTFITS')
    OUTFITS_list = [f'OUTFITS/{f}' for f in os.listdir(outfits_dir) if f.endswith(('.png',))]  # Prepend 'BG/' to each filename

    eyes_dir = os.path.join('static', 'EYES')
    EYES_list = [f'EYES/{f}' for f in os.listdir(eyes_dir) if f.endswith(('.png',))]  # Prepend 'BG/' to each filename


    return render(request, "home.html", {"BG_list": BG_list, 
        "Hands_list": Hands_list,   
        "OUTFITS_list": OUTFITS_list,
        "EYES_list": EYES_list})

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>

        testing
        </body>

    </html>
    '''
    return HttpResponse(html)