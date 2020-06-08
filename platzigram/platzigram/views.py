#Django
from django.http import HttpResponse
from django.http import JsonResponse

#Utilities
from datetime import datetime
import json

def _order_list(arr):
    pass


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y- %H:%M')
    return HttpResponse(f"Hello, world!. The time in the server is: {now}")

def sort_integers(request):
    """Return a JSON response with sorted integers"""
    #import pdb;  pdb.set_trace()
    numbers = sorted(list(map(int, (request.GET['numbers']).split(","))))
    #Alternativa 1
    response = JsonResponse(numbers,safe=False)
    #Alternativa 2 -Tiene un estilo más semejante al usado en una API
    data = {
        'status': 'OK',
        'numbers': numbers,
        'message': 'Numbers sorted'
    }

    #Hay dos formas de hacer el return
    #Directamente mandando la variable de JsonResponse()
   # return response
    #O usando la función HttpResponse con un atributo que especifique el formato JSON
    return HttpResponse(json.dumps(data)    , content_type="application/json")

def say_hi(response, name, age):
    """Return greeting"""
    response = HttpResponse()
    if age < 12:
        message = "Sorry {}, you are not allowed here".format(name)
    else:
        message = "Hi, {}, welcome to platzigram".format(name)
    
    
    #response.write(message)
    return HttpResponse(message)
