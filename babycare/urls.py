from django.conf.urls import url
from django.contrib import admin
from django.template.context_processors import static

from django.conf import settings
from django.conf.urls.static import static
from care import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name='homepage'),

    url(r'^about/$', views.AboutView.as_view(), name='catalogue'),
    url(r'^cooperation/$', views.CooperationView.as_view(), name='cooperation'),
    url(r'^brands/$', views.BrandsView.as_view(), name='brands'),
    url(r'^certificates/$', views.CertificateView.as_view(), name='certificates'),
    url(r'^articles/$', views.ArticleView.as_view(), name='article'),


    url(r'^catalogue/$', views.CatalogueView.as_view(), name='catalogue'),
    url(r'^product/$', views.ProductView.as_view(), name='product'),

    url(r'^contacts/$', views.ContactView.as_view(), name='contact'),
    url(r'^map/$', views.MapView.as_view(), name='map'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
