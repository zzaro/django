from django.contrib import admin
from django.urls import path, include
from midterm.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lib/', include('library.urls')),
    path('members/', include('members.urls')),
    path('', HomeView.as_view(), name='home'),
]
