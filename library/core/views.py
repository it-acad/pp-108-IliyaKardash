from django.shortcuts import render


def starting_page(request):
    return render(request, 'starting_page.html')


def home_view(request):
    return render(request, 'home.html')
