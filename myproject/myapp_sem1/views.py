# from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse(f'<h1>Это страница игры монетки</h1>')

def coin(request):
    logger.info('Index page accessed')
    result = random.choice(['Орел', 'Решка'])
    return HttpResponse(f'Выпало значение {result}')

def random_number(request):
    logger.info('Index page accessed')
    result = random.randint(1, 100)
    return HttpResponse(f'Выпало значение {result}')

def random_roll(request):
    logger.info('Index page accessed')
    result = random.randint(1, 6)
    return HttpResponse(f'Выпало значение {result}')