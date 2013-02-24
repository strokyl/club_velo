from models import Velo
from django.template.response import TemplateResponse

def index(request):
    velos = Velo.objects.filter(louable=True,louer=False)

    return TemplateResponse(request, 'index.html', {'velos':velos})

def horaires(request):
    return TemplateResponse(request, 'horaires.html')

def contact(request):
    return TemplateResponse(request, 'contact.html')
# Create your views here.
