from django.shortcuts import render


def starting_page(request):
    return render(request, 'starting_page.html')
