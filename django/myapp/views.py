from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django PoC!")

def detail(request, item_id):
    return HttpResponse(f"Details for item {item_id}")
