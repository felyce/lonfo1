from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Lonfoapp1
 
 
class Lonfoapp1ListView(ListView):
    model = Lonfoapp1

class Lonfoapp1DetailView(DetailView):
    model = Lonfoapp1 