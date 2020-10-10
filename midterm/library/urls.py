from django.urls import path
from library.views import LibraryLV, LibraryDV

app_name = 'library'
urlpatterns = [
    path('', LibraryLV.as_view(), name='index'),
    path('<int:pk>/', LibraryDV.as_view(), name='detail'),
]
