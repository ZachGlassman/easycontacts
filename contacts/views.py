from django.http import HttpResponse

def index(request):
    return HttpResponse("hello")
    
def person_detail(request, person_id):
    return HttpResponse("this is person {}".format(person_id))