from django.urls import path,include
from .api import RegisterApi
from .views import RegisterAPIView,LoginAPIView,IndexPageView
from . import views
urlpatterns=[
    # path('api/register',RegisterApi.as_view()),
    path('regi/',RegisterAPIView.as_view(),name='regi'),
    path('log/',LoginAPIView.as_view(),name='logg'),
    path('greeting/',IndexPageView.as_view(),name='greeting')
    # path('register/',views.register,name='reg'),
    # path('login/',views.login,name='log')
]