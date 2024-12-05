from django.http import HttpResponse
from django.db.models import Q
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User 

class SearchResultsView(ListView):
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = User.objects.filter(
            Q(username__contains=query)
        )
        return object_list
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def users(request):
  template = loader.get_template('users.html')
  return HttpResponse(template.render())

def homepage(request):
    return render(request, 'homepage.html')

def yava(request):
  template = loader.get_template('yava.html')
  return HttpResponse(template.render())

def pavlusha(request):
  template = loader.get_template('pavlusha.html')
  return HttpResponse(template.render())

def popup(request):
  template = loader.get_template('popup.html')
  return HttpResponse(template.render())

def error404(request, exception):
    return render(request, '404.html', status=404)

def error500(request):
    return render(request, '500.html', status=500)

def error400(request, exception):
    return render(request, '400.html', status=400)

def error403(request, exception):
    return render(request, '403.html', status=403)

def events(request):
  template = loader.get_template('events-not-made.html')
  return HttpResponse(template.render())

def projects(request):
  template = loader.get_template('projects-not-made.html')
  return HttpResponse(template.render())

def freerobux(request):
  return redirect("https://www.youtube.com/watch?v=uzzJco0P97M")