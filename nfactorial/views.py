from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse



# Create your views here.

def index(request):
    return HttpResponse("Hello, nfactorial school!")

def add(request, first: int, second: int):
    return HttpResponse(f"{first + second}")

def upper(request, text: str):
    return HttpResponse(f"{text.upper()}")

def palindrome(request, word: str):
    return HttpResponse(word == word[::-1])

def calculator(request, first: int, operation: str, second: int):
    res = ""

    if operation == "add":
        res = f"{first + second}"

    elif operation == "sub":
        res = f"{first - second}"

    elif operation == "div":
        res = f"{first / second}"

    elif operation == "mult":
        res = f"{first * second}"

    else:
        res = "I dont know this operation yet"

    return HttpResponse(res)
    
