from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path("register/", register, name="register"),
    path("my_cars/", my_cars, name="my_cars"),
    path("my_records/", my_records, name="my_records"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
