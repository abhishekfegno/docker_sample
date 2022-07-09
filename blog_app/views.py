from django.views.generic import TemplateView
from . models import Blog

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


