
from django.contrib import admin
from django.urls import path
from uyishi.views import uyishi_list
from dars.views import dars_list
from telefon.views import telefon_list
from komputer.views import komputer_list
from rang.views import rang_list
from maxsulot.views import maxsulot_list
from shaxar.views import shaxar_list
from poyezd.views import poyezd_list
urlpatterns = [
    path('poyezd/',poyezd_list),
    path('shaxar/',shaxar_list),
    path('maxsulot/',maxsulot_list),
    path('rang/',rang_list),
    path('komp/',komputer_list),
    path('tel/',telefon_list),
    path('dars/',dars_list),
    path('uy/', uyishi_list),
    path('admin/', admin.site.urls),
]
