from django.shortcuts import render


def catalogs_home(request):
    return render(request, 'catalogs/catalogs.html')
