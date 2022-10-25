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