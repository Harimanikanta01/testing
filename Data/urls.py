from django.contrib import admin
from django.urls import path
from newapp.views import *
from newapp.views import Ma
from django.conf import settings
from django.conf.urls.static import static
from newapp.views import Ban
from newapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
     path('products/',Li.as_view(),name="get"),
    path('add/',Va.as_view(),name="post"),
    path('retrive/<int:pk>/',Ma.as_view(),name="retrive"),
    path('delete/<int:pk>/',De.as_view(),name="DELETE"),
    path('banner/',Ban.as_view(),name="banner"),
    path('account/',Cr.as_view(),name="create"),
    path('circle/',Ct.as_view(),name="topcircle"),
    path('product1/',P111.as_view(),name="product1"),
      path('product2/',P222.as_view(),name="product2"),
      path('add1/',Addd.as_view(),name="add"),
      path('discount/',Discount12.as_view(),name="disacount"),
      path('mobile/',Mobile12.as_view(),name="mobile"),
      path('mr/<int:pk>/',Mobile13.as_view(),name="mobile"),
      path('cart/',Cart1.as_view(),name='cart'),
      path('p3/',product123.as_view(),name="all"),
      path('p67/',P451.as_view(),name="all1"),
      path('p90/',Mobile135.as_view(),name="all12"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)