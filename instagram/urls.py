from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('home/',views.home,name='home'),
    path('profile/<username>/',views.profile,name='profile'),
    path('user/<username>/',views.user,name='user'),
    path('search/', views.search, name='search'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)