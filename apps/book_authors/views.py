from django.shortcuts import render, redirect

def index( request ):
    return render( request, "book_authors/index.html")
    

# Create your views here.
