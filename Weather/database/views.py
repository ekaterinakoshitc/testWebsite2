from django.shortcuts import render,redirect
from .models import CityBase, TemperatureBaseOn
from django.views.generic import DeleteView
from .forms import *
# Create your views here.

def cityMetod(request):
    cityForm = CityBase.objects.order_by('name_city')
    return render(request,'database/city.html',{'cityForm':cityForm})

def tempMetod(request):
    tempForm = TemperatureBaseOn.objects.order_by('date')
    return render(request,'database/temp.html',{'tempForm':tempForm})

def createcity(request):
    error=''
    t=''
    if request.method == 'POST':
        form = CityBaseForm(request.POST)
        if form.is_valid():
            z=request.POST['name_city']
            t = CityBase.objects.get_or_create(name_city=z)
            if t=='':
                return redirect('city')
            else:
                error = 'Ошибка заполнения'

        else:
            error='Ошибка заполнения'
    form = CityBaseForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request,'database/create_city.html',data)


def createtemp(request):
    error=''
    t=''
    if request.method == 'POST':
        form = TempAddForm(request.POST)
        city = CityBase.objects.get(id=request.POST['i_city'])
        try:
            TemperatureBaseOn.objects.create(i_city=city,temperaturedata=request.POST['temperaturedata'], date = request.POST['date'], t= request.POST['t'])
            return redirect('temp')
        except:
            error = 'Ошибка заполнения'

    form = TempAddForm()
    data={
        'form': form,
        'error': error
    }
    return render(request, 'database/create_temp.html', data)


def findtemp(request):
    error=''
    if request.method == 'POST':
        form = TempBaseFindForm(request.POST)
        city = CityBase.objects.get(id=request.POST['i_city'])
        dateP = request.POST.get('datepicker')
        if form.is_valid():
            form=''
            form = TemperatureBaseOn.objects.filter(i_city =city, date= dateP)

    form = TempBaseFindForm()
    data={
        'form': form,
        'error': error
    }
    return render(request, 'database/chart.html', data)

def deletecity(request):

    error=''
    if request.method == 'POST':
        form = CityBaseForm(request.POST)
        z=request.POST['id']
        city = CityBaseForm.objects.get(id=z)
        city.delete()
    form = CityBaseForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request,'database/city.html',data)

def deletetemp(DeleteView):
        model = TemperatureBaseOn
        success = '/temp/'
        template_name ='database/deletetemp.html'

