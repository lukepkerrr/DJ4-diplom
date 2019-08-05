from django.shortcuts import render
from .models import Item, Section, Jumbotron, Item_in_cart
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def update_cart(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST['user-id'])
        item = Item.objects.get(id=request.POST['item-id'])
        try:
            item_in_cart = Item_in_cart.objects.get(item=item, user=user)
        except ObjectDoesNotExist:
            item_in_cart = Item_in_cart.objects.create(item = item, user=user, amount=0)
        item_in_cart.amount += 1
        item_in_cart.save()

# Create your views here.
def main_page(request):
    template = 'Shop/index.html'
    context = {'jumbotron': Jumbotron.objects.all()}
    update_cart(request)
    return render(request, template, context)


def cart(request):
    user = User.objects.get(id=request.GET.get('id'))
    items_in_cart = Item_in_cart.objects.filter(user=user)
    amount_of_items = len(items_in_cart)
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
    update_cart(request)
    section_id = request.GET.get('id')
    template = 'Shop/section.html'
    context = {'section': Section.objects.get(id=section_id)}
    return render(request, template, context)


def item(request):
    update_cart(request)
    item_id = request.GET.get('id')
    template = 'Shop/item.html'
    context = {'item': Item.objects.get(id=item_id)}
    return render(request, template, context)