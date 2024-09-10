from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Website
from .models import Order
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def menu(request):
    return render(request,'menu.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def place_order(request):
    if request.method == 'POST':
        customer_name = request.POST.get('name')
        customer_email = request.POST.get('email')
        coffee_type = request.POST.get('coffee')
        quantity = request.POST.get('quantity')

        if customer_name and customer_email and coffee_type and quantity:
            quantity = int(quantity)  # Convert quantity to integer
            total_price = calculate_total_price(coffee_type, quantity)  # Define this function as needed

        # Create and save the new order
        order = Order(
            customer_name=customer_name,
            customer_email=customer_email,
            coffee_type=coffee_type,
            quantity=quantity,
            total_price=total_price
        )
        order.save()

        # Redirect or render a success page
        return redirect('order_success')

    return render(request, 'place_order.html')

def order_success(request):
    # Example context data (replace with actual data retrieval logic)
    order = {
        'id': 12345,
        'date': '2024-09-02',
        'total_amount': 100.00,
    }
    return render(request, 'order_success.html', {'order': order})