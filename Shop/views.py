from django.shortcuts import render, get_object_or_404
from .models import Item, Section, Jumbotron, ItemInCart
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def update_cart(request):
    user = request.user
    item = Item.objects.get(id=request.POST['item-id'])
    try:
        item_in_cart = ItemInCart.objects.get(item=item, user=user)
    except ObjectDoesNotExist:
        item_in_cart = ItemInCart.objects.create(item = item, user=user, amount=0)
    item_in_cart.amount += 1
    item_in_cart.save()

# Create your views here.
def main_page(request):
    template = 'Shop/index.html'
    context = {'jumbotron': Jumbotron.objects.all()}
    if request.method == 'POST':
        update_cart(request)
    return render(request, template, context)


def cart(request):
    if request.method == 'POST':
        print('Заказ сделан')
        ItemInCart.objects.filter(user=request.user).delete()
    items_in_cart = ItemInCart.objects.filter(user=request.user)
    amount_of_items = items_in_cart.count()
    template = 'Shop/cart.html'
    context = {
        'items': items_in_cart,
        'amount': amount_of_items
    }
    return render(request, template, context)


def empty_section(request):
    template = 'Shop/empty_section.html'
    context = {}
    return render(request, template, context)


def section(request):
    if request.method == 'POST':
        update_cart(request)
    section_id = request.GET.get('id')
    template = 'Shop/section.html'
    context = {'section': Section.objects.get(id=section_id)}
    return render(request, template, context)


def item(request):
    if request.method == 'POST':
        update_cart(request)
    item_id = request.GET.get('id')
    template = 'Shop/item.html'
    context = {'item': get_object_or_404(Item, id=item_id)}
    return render(request, template, context)