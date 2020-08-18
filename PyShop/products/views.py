from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """
    docstring: use index as a main page
    :param request:
    :return:
    """
    return HttpResponse('Hello World')

# after we create view function, we need to map URL to that function
# /products URL --> index function
# URL means Uniform Resource Locator (Address)
# now views file is done, go to urls python file


def new(request):
    return HttpResponse('New Products')
