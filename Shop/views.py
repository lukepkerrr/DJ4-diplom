from django.shortcuts import render, get_object_or_404
from .models import Item, Section, Jumbotron, ItemInCart, PurchasedItem
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
        items_for_purchase = ItemInCart.objects.filter(user=request.user)
        for purchasing_item in items_for_purchase:
            new_item = PurchasedItem(
                item=purchasing_item.item,
                user=purchasing_item.user,
                amount=purchasing_item.amount
            )
            new_item.save()
        items_for_purchase.delete()
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