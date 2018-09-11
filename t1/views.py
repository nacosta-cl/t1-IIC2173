from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    response = JsonResponse({'Bienvenido':'Emite un comentario con un request GET en el siguiente formato'})
    return response
    #return HttpResponse("Bienhallado el que se aventura en este server. Para enviar un comentario, emite un request HTTP GET con el siguiente formato")
