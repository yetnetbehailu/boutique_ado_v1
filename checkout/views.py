from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KIdChHYTYZ8t0z67oQumiUihrq9bv5WNBMdpIDRiZrluIERl4vDRA04LAnrHNZ9GGsRmpzNNrzF5lGSFRp0ijz3009NpUvJFz',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
