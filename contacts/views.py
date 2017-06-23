from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Person
from .forms import PersonForm

@login_required
def index(request):
    person_list = Person.objects.order_by('name')
    context = {'person_list':person_list}
    return render(request, 'contacts/index.html', context)
   
@login_required
def person_detail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    form = PersonForm({'person':person})
    return render(request, 'contacts/detail.html', {'person':person,'form':form})
 
@login_required
def update(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.email = request.POST['email']
    person.employer = request.POST['employer']
    person.save()
    return render(request, 'contacts/detail.html', {'person': person})