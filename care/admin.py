from django.contrib import admin
from django.forms import forms, ModelChoiceField

from care.models import Article, Certificate, Brand, Product, Contact, Map, About, Menu, SubMenu, Pages, Banner, Task


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date')
    list_filter = ['date']
    search_fields = ['text']


class CertificatesAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date')
    list_filter = ['date']
    search_fields = ['text']


class BrandsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date')
    list_filter = ['date']
    search_fields = ['text']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'price', 'date')
    list_filter = ['date']
    search_fields = ['text']


class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'phone', 'email')
    search_fields = ['address']


class MapAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'phone', 'description')
    search_fields = ['description']


class AboutAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone', 'description']
    search_fields = ['description']


class MenuAdmin(admin.ModelAdmin):
    list_display = ['title']


class SubMenuAdmin(admin.ModelAdmin):
    list_display = ['title']


class PagesAdmin(admin.ModelAdmin):
    list_display = ['title']







admin.site.register(Article, ArticleAdmin)
admin.site.register(Certificate, CertificatesAdmin)
admin.site.register(Brand, BrandsAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Map, MapAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
admin.site.register(Pages, PagesAdmin)
admin.site.register(Banner)
admin.site.register(Task)
