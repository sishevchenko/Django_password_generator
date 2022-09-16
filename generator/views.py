# Create your views here.
import string

from django.shortcuts import render
import random


def home(request):
    return render(request, "home.html")


def password(request):
    characters = ''

    if request.GET.get('uppercase'):
        characters += string.ascii_uppercase
    if request.GET.get('lowercase'):
        characters += string.ascii_lowercase
    if request.GET.get('numbers'):
        characters += string.digits
    if request.GET.get('special'):
        characters += '!@#$%^&*?№'

    if len(characters) == 0:
        return render(request, "missing.html")

    length = int(request.GET.get('length', 12))

    password = []

    for _ in range(length):
        password.append(random.choice(characters))

    password = ''.join(password)

    return render(request, "password.html", {'password': password})


def self_info(request):
    return render(request, "self_info.html")
