from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Visitor, Paper
from .forms import PaperForm

def index(request):
    return render(request,'mainapp/index.html')


class RegisterVistor(SuccessMessageMixin,CreateView):
    model = Visitor
    fields = ['name', 'phone','email', 'organisation', 'address']
    success_url = reverse_lazy('index')
    success_message = 'Thank you for Request We contact Soon'


class RegisterPaper(SuccessMessageMixin,CreateView):
    model = Paper
    form_class = PaperForm
    # fields = ['name','lname', 'phone','email', 'organisation', 'department','comments','cname','ccity','file']

    success_url = reverse_lazy('index')
    success_message = 'Thank you for Request We contact Soon'
    def form_valid(self, form):
        file_up=Paper(file=self.get_form_kwargs().get('files')['file_up'])
        file_up.save()
        self.id=file_up.id
