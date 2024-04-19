from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("login/", log_in, name="login"),
    path("logout/", user_logout, name="logout"),
    path("my_cars/", my_cars, name="my_cars"),
    path("my_records/", my_records, name="my_records"),
    path("addrecord/<int:pk>", addrecord, name="addrecord"),
    path("delrecord/<int:pk>", delrecord, name="delrecord"),
    path("carrecords/<int:pk>", carrecords, name="carrecords"),
    path('update_mileage/<int:pk>', UpdateMileage.as_view(), name='update_mileage'),
    path('create_car/', create_car, name='create_car'),
    path("delcar/<int:pk>", delcar, name="delcar"),
    path("delnotification/<int:pk>", delnotification, name="delnotification"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
