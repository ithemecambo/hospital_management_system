from django.shortcuts import render


def index(request):
    context = {
        'title': 'Hospital Management System',
        'queryset': 'Home'
    }
    return render(request, 'hospital/index.html', context)
