from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Order
from .models import Book
from authentication.models import CustomUser
from django.utils import timezone


def is_librarian(user):
    return user.is_authenticated and user.role == 1


def all_orders(request):
    if is_librarian(request.user):
        orders = Order.objects.all().select_related('book', 'user')
        return render(request, 'order/all_orders.html', {'orders': orders})
    return redirect('home')


def create_order(request):
    if not request.user.is_librarian:
        return redirect('home')

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        book_id = request.POST.get('book_id')
        plated_end_at = request.POST.get('plated_end_at')

        try:
            user = CustomUser.objects.get(id=user_id)
            book = Book.objects.get(id=book_id)

            order = Order.create(user=user, book=book,
                                 plated_end_at=plated_end_at)

            if order:
                messages.success(request, 'Order was placed')
            else:
                messages.error(
                    request, 'This book is already ordered or not available')
        except CustomUser.DoesNotExist:
            messages.error(request, 'User not found')
        except Book.DoesNotExist:
            messages.error(request, 'Book not found')
    users = CustomUser.objects.all()
    books = Book.objects.all()

    return render(request, 'order/create_order.html', {'users': users, 'books': books})


def close_order(request, order_id):
    if not request.user.is_authenticated or not request.user.is_librarian:
        return redirect('home')

    try:
        order = Order.objects.get(id=order_id, end_at__isnull=True)
        order.end_at = timezone.now()
        order.save()
        messages.success(request, 'Order closed successfully')
    except Order.DoesNotExist:
        messages.error(request, 'Order has not been found')

    return redirect('all_orders')


def my_orders(request):
    if not is_librarian(request.user):
        orders = Order.objects.filter(user=request.user)
        return render(request, 'order/my_orders.html', {'orders': orders})
    return redirect('home')
