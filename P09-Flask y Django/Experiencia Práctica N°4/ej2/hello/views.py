from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
  
def addrecord(request):
  x = int(request.POST['first'])
  y = int(request.POST['last'])
  member = Members(num1=x, num2=y, suma=x+y, resta=x-y, multi=x*y, div=x/y, poten=x**y)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = int(request.POST['first'])
  last = int(request.POST['last'])
  member = Members.objects.get(id=id)
  member.num1 = first
  member.num2 = last

  member.suma = first+last
  member.resta = first-last
  member.multi = first*last
  member.div = first/last
  member.poten = first**last

  member.save()
  return HttpResponseRedirect(reverse('index'))