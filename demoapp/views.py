from django.http import HttpResponse
from django.shortcuts import render
from.models import Place
from.models import Team

# Create your views here.
def home(request):
    obj=Place.objects.all()
    team=Team.objects.all()
    return render(request,"index.html",{'result':obj,'person':team})
#def about(request):
  #  return HttpResponse("This page is for about")
#def contact(request):
 #   return render(request,"contact.html")
#def detail(request):
#    return HttpResponse("This page is for showing details")
#def thanks(request):
 #   return render(request,"thanks.html")