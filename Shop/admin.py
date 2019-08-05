from django.contrib import admin

from .models import Item, Type, Section, Item_in_cart, Jumbotron, Comment

from django.contrib.auth.models import User

class ItemInline(admin.TabularInline):
    model = Item_in_cart
    extra = 1


class ItemAdmin(admin.ModelAdmin):
    pass


class TypeAdmin(admin.ModelAdmin):
    pass


class SectionAdmin(admin.ModelAdmin):
    pass


class JumbotronAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


class UserAdmin(admin.ModelAdmin):
    inlines = (ItemInline, )


class Item_in_cartAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Jumbotron, JumbotronAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Item_in_cart, Item_in_cartAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)