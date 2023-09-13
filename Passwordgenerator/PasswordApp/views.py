from django.shortcuts import render
import random


def generate(request):
    return render(request, 'PasswordApp/generator.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('Numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length',12))

    thepass = ''
    for x in range(length):
        thepass += random.choice(characters)

    return render(request, 'PasswordApp/password.html', {'password' : thepass})
