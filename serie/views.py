from django.shortcuts import render
from . import forms
from . import models
# Create your views here.

def cadastro(request):
    form = forms.SerieForm()
    if request.method == 'POST':
        form = forms.SerieForm(request.POST)
        if form.is_valid():
            print("Saving...")
            form.save(commit=True)
        else:
            print("ERROR")
    series_list=models.Serie.objects.order_by('nome')
    data_dict={"serie_records":series_list,'form':form}

    return render(request,'serie/serie.html',data_dict)

def delete(request,id):
    try:
        models.Serie.objects.filter(id=id).delete()
        form = forms.SerieForm()
        series_list = models.Serie.objects.order_by('nome')
        data_dict = {"serie_records":series_list,'form':form}
        return render(request,'serie/serie.html',data_dict)
    except:
        return HttpResponseNotAllowed();
