from django.shortcuts import render, redirect
def index( request ):
    return render( request, "dojo_ninjas/index.html")