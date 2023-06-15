from django.shortcuts import render

# Create your views here.

def index(request):
    
    context = {
        'zones': {
            'zone_1': True,
            'zone_2': True,
            'zone_3': False,
            'zone_4': True,
        },
        'temp': 'temp'
    }
    return render(request, 'garden_app/index.html', context)