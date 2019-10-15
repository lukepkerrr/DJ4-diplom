from django.contrib import admin

from .models import Item, Type, Section, ItemInCart, PurchasedItem, Jumbotron, Comment

from django.contrib.auth.models import User


class ItemInline(admin.TabularInline):
    model = ItemInCart
    extra = 1


class PurchasedItemInline(admin.TabularInline):
    model = PurchasedItem
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
    inlines = (ItemInline, PurchasedItemInline)


class ItemInCartAdmin(admin.ModelAdmin):
    pass


class PurchasedItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Jumbotron, JumbotronAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ItemInCart, ItemInCartAdmin)
admin.site.register(PurchasedItem, PurchasedItemAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)