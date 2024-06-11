from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return render(request, 'myapp_hw1/main.html')


def about(request):
    logger.info('Index page accessed1')
    return render(request, 'myapp_hw1/data.html')
