from .models import Type


def func_for_menu(request):
    return {'types': Type.objects.all()}