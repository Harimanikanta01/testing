

# Create your views here.
from .serializer import Jay
from .models import Nari
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView
from .models import Nari
from .serializer import Jay
from rest_framework.request import Request
from .models import Banner
from .serializer import Ba
from .serializer import *
from rest_framework.generics import RetrieveAPIView
from .models import Create
from rest_framework.response import Response
import requests

from rest_framework.views import APIView
from io import BytesIO
class Li(ListAPIView):
    queryset = Nari.objects.all() 
    serializer_class = Jay 
class Va(CreateAPIView):
    queryset=Nari.objects.all()
    serializer_class=Jay
class Ma(RetrieveAPIView):
        queryset=Nari.objects.all()
        serializer_class=Jay
class De(DestroyAPIView):
    queryset=Nari.objects.all()
    serializer_class=Jay
class Ban(ListAPIView):
     queryset=Banner.objects.all()
     serializer_class=Ba
class Cr(ListAPIView):
     queryset=Create.objects.all()
     serializer_class=Cre
class Ct(ListAPIView):
     queryset=Circle.objects.all()
     serializer_class=Cir
class P111(ListAPIView):
     queryset=P1.objects.all()
     serializer_class=P11
class P222(ListAPIView):
     queryset=P2.objects.all()
     serializer_class=P22
class Addd(ListAPIView):
     queryset=Add.objects.all()
     serializer_class=add1
class Discount12(ListAPIView):
     queryset=Discount.objects.all()
     serializer_class=Discount1
class Mobile12(ListAPIView):
     queryset=Mobile.objects.all()
     serializer_class=Mobile1

class Mobile13(RetrieveAPIView):
     queryset=Mobile.objects.all()
     serializer_class=Mobile1
class Cart1(CreateAPIView):
     queryset=Cart
     serializer_class=Cart12
class product123(ListAPIView):
     queryset=product3.objects.all()
     serializer_class=product31
class P451(CreateAPIView):
     queryset=P1.objects.all()
     serializer_class=P11
class Mobile135(CreateAPIView):
     queryset=Mobile.objects.all()
     serializer_class=Mobile1

