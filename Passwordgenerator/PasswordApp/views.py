from django.shortcuts import render
import random


def generate(request):
    return render(request, 'PasswordApp/generator.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.entend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        characters.entend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.entend(list('0123456789'))

    length = int(request.GET.get('length',12))

    thepass = ''
    for x in range(length):
        thepass += random.choice(characters)

    return render(request, 'PasswordApp/password.html', {'password' : thepass})
