
from django.shortcuts import render, redirect
from .models import Noticia
from .forms import NoticiaForm

def listarNoticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticia/listarNoticias.html', {'noticias': noticias})

def adicionarNoticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarNoticias')
    else:
        form = NoticiaForm()
    return render(request, 'noticia/adicionarNoticia.html', {'form': form})
