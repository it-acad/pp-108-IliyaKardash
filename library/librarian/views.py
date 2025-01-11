from django.shortcuts import render, get_object_or_404
from authentication.models import CustomUser
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


@login_required
def all_users(request):
    if not request.user.is_librarian:
        return render(request, 'librarian/403.html', {'error': 'You do not have access to this page.'})

    users = CustomUser.objects.all()
    return render(request, 'librarian/all_users.html', {'users': users})


@login_required
def view_user(request, id):
    if not request.user.is_librarian:
        return render(request, 'librarian/403.html', {'error': 'You do not have access to this page.'})

    user = get_object_or_404(CustomUser, id=id)
    return render(request, 'librarian/view_user.html', {'user': user})
