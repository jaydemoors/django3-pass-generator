from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password':'1q2w3e4r5t'})

def password(request):
    myRandomPass = ''
    passChars = list('abcdefghijklmnopqrstuvwxyz')
    passLength = int(request.GET.get('length',12))

    if (request.GET.get('uppercase')):
        chars = 'abcdefghijklmnopqrstuvwxyz'
        upperChars = chars.upper()
        passChars.extend(list(upperChars))
    if (request.GET.get('numbers')):
        numValues = '0123456789'
        passChars.extend(list(numValues))
    if (request.GET.get('special')):
        specialChars = '!$*@#'
        passChars.extend(list(specialChars))

    for x in range(passLength):
        myRandomPass += random.choice(passChars)

    return render(request, 'generator/password.html', {'password':myRandomPass})

def about(request):
    return render(request, 'generator/about.html')
