from django.urls import path
from .views import hellodjango, get_current_date, say_hello, get_year, get_month, get_day

urlpatterns = [
    path('',  hellodjango),
    path('date/', get_current_date),
    path('<str:name>/', say_hello),
    path('date/year/', get_year),
    path('date/month/', get_month),
    path('date/day/', get_day),
]
