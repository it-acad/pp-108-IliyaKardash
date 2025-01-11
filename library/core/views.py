from django.shortcuts import render, redirect


def starting_page(request):
    return render(request, 'starting_page.html')


def home_view(request):

    if request.user.is_authenticated:
        role = request.user.role
        return render(request, 'home.html', {'role': role})
    else:
        return redirect('login')
