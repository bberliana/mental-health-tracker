from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165875',
        'name': 'Rania Berliana',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)