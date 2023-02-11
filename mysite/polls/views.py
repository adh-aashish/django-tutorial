from django.http import HttpResponse

def index(request):             
    message = "Hello, world. Your at the polls index"
    return HttpResponse(message) #type: ignore
