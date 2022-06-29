from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from . import utils, models

# Create your views here.
def home_page(request):
    return render(request, 'shortener/index.html')

def create_short_link(request):
    print(request.method)
    if(request.method == "POST"):
        url = request.POST['url']
        shortener = utils.get_shortener_by_url(url)

        if(shortener != None):
            return render(request, 'shortener/display.html', {'link': "http://127.0.0.1:8000/" + shortener.short_link})
        

        link = utils.generate_short_link()
        
        shortener = models.UrlShortener(url=url, short_link=link)
        shortener.save()

        context = {
            'link': "http://127.0.0.1:8000/" + shortener.short_link
        }

        return render(request, 'shortener/display.html', context)
        
    return redirect('home')

def redirect_short_link(request, link):
    shortener = utils.get_shortener_by_link(link)

    if(shortener == None):
        return redirect('home')
    else:
        return redirect(shortener.url)