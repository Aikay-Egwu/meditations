from django.shortcuts import render
from django.views import View
from .forms import AddRhemaForm
# Create your views here.

class Home(View):
  template_name = 'rhema/index.html'

  def get(self, request):
    return render(request, self.template_name)

class CreateNew(View):
  template_name = 'rhema/add.html'

  def get(self, request):
    form = AddRhemaForm()
    context = {'form': form}
    return render(request, self.template_name, context)