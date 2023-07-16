from urllib.request import Request
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.template import RequestContext
from django.template.context import Context
from django.http import JsonResponse
from .forms import *
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.template import loader
import random
import string


def generate_random_file_name(length=15):
    """
        Générer des noms aleatoire pour les fichiers avant stockage
    """
    letters = string.ascii_letters
    random_name = ''.join(random.choice(letters) for _ in range(length))
    return random_name


# Create your views here.
def accueil(request):
    message = ""
    form = EtudiantForm()
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            carte_etudiant_name = generate_random_file_name() + '.pdf'
            carte_cni_name = generate_random_file_name() + '.pdf'
            
            form.instance.carte_etudiant.name = carte_etudiant_name
            form.instance.carte_cni.name = carte_cni_name
            etudiant = form.save()
            form = EtudiantForm()
            message = "success"
        else:
            message = "error"
    return render(request, 'app/index.html', {'form': form, 'message': message})
