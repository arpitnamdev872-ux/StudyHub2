from django.shortcuts import render

def home(request):
    query = request.GET.get('q')

    context = {
        'query': query
    }

    return render(request, 'app/index.html', context)