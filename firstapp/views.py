from django.http import HttpResponse
import datetime


def hellodjango(request):
    return HttpResponse("Hello Django!")


def say_hello(request, name):
    return HttpResponse(f"Hello {name}!")


def get_date():
    date = datetime.datetime.now()
    return date


def get_current_date(request):
    return HttpResponse(f"Current date is {get_date().strftime('%d.%m.%Y')}")


def get_year(request):
    return HttpResponse(f"Current year is {get_date().strftime('%Y')}")


def get_month(request):
    return HttpResponse(f"Current month is {get_date().strftime('%m')}")


def get_day(request):
    return HttpResponse(f"Current day is {get_date().strftime('%d')}")
