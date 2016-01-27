from django.contrib import admin
from care.models import Article, Certificate, Brand, Product, Contact, Map, About


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
    list_display = ('title', 'address', 'phone', 'description')
    search_fields = ['description']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Certificate, CertificatesAdmin)
admin.site.register(Brand, BrandsAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Map, MapAdmin)
admin.site.register(About, AboutAdmin)
