from django.shortcuts import render, redirect
from .models import Note

def index(request):
    # tasks = Task.objects.all()
    # tasks = Task.objects.order_by('-title')  # - обратный порядок
    #tasks = Task.objects.order_by('title')[:1]  # срез, как выбор сколько записей

    notes = Note.objects.order_by('id')
    info_notes = []

    for i in notes:
        if i.note_type == 'info': info_notes.append(i)

    return render( request, 'main/index.html',
            { 'title': 'Главная страница сайта',
              'notes': info_notes,
            }
                 )

def about_us(request):
    return render( request, 'main/about.html' )

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
