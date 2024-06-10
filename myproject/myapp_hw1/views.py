from django.shortcuts import render
from django.http import HttpResponse
import logging
from django.template.loader import render_to_string

logger = logging.getLogger(__name__)

def index(request):
    response = render_to_string('myapp_hw1/main1.html')
    logger.info('Index page accessed')
    return HttpResponse(response)


def about(request):
    logger.info('Index page accessed')
    response = render_to_string('myapp_hw1/data.html')
    return HttpResponse(response)
