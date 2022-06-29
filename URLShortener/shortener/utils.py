import random
from . import models
from django.core.exceptions import ObjectDoesNotExist

def generate_short_link():
    regex = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    link = ""

    for i in range(5):
        piece = random.randrange(0, regex.__len__())
        link += regex[piece]
    
    if(validate_link(link)):
        return link
    else:
        return generate_short_link()

def validate_link(link):
    shortener = get_shortener_by_link(link)

    if(shortener == None):
        return True
    else:
        return False

def get_shortener_by_link(link):
    try:
        shortener = models.UrlShortener.objects.get(short_link=link)
    except ObjectDoesNotExist:
        return None
    else:
        return shortener

def get_shortener_by_url(url):
    try:
        shortener = models.UrlShortener.objects.get(url=url)
    except ObjectDoesNotExist:
        return None
    else:
        return shortener