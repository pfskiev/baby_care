from django.views import generic
from care.models import Article, Certificate, Brand, Product, Contact, Map, About


class IndexView(generic.ListView):
    template_name = 'care/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.order_by('date')[:100]


class ArticleView(generic.ListView):
    template_name = 'care/articles.html'

    def get_queryset(self):
        return Article.objects.order_by('date')[:100]


class CertificateView(generic.ListView):
    template_name = 'care/certificates.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Certificate.objects.order_by('date')[:100]


class BrandsView(generic.ListView):
    template_name = 'care/brands.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Brand.objects.order_by('date')[:100]


class CatalogueView(generic.ListView):
    template_name = 'care/catalogue.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Product.objects.order_by('date')[:100]


class CooperationView(generic.ListView):
    template_name = 'care/cooperation.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Product.objects.order_by('date')[:100]


class ProductView(generic.ListView):
    template_name = 'care/product.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Product.objects.order_by('date')[:100]


class ContactView(generic.ListView):
    template_name = 'care/contacts.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Contact.objects.order_by('phone')[:100]


class MapView(generic.ListView):
    template_name = 'care/map.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Map.objects.order_by('phone')[:100]


class AboutView(generic.ListView):
    template_name = 'care/about.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return About.objects.order_by('phone')[:100]
