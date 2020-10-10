from django.urls import path
from members.views import MembersLV, MembersDV


app_name = 'members'
urlpatterns = [
    path('', MembersLV.as_view(), name='index'),
    path('<int:pk>/', MembersDV.as_view(), name='detail'),
]