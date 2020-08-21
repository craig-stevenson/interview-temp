from django.shortcuts import render
from django.http import JsonResponse
import psutil
# Create your views here.
def api(request):
    response = {
        'cpu_percent': psutil.cpu_percent(),
        'virtual_memory': psutil.virtual_memory()._asdict(),
    }
    return JsonResponse(response)

def home(request):
    return render(request, 'hq/index.html', context={})