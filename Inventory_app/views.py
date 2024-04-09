from django.shortcuts import render, redirect
from .models import Trackin
from .forms import Traking_forms
from tabulate import tabulate

def index(request):
    name = Trackin.objects.all()
    data = []
    for i in name:
        formated_value = "{:.2f}".format(i.value)
        x = str(f"${formated_value}")
        data.append([i.name,i.serial_number,x])

    html_table = tabulate(data, headers=["NAME","Serial Number ","Value"], tablefmt="github")
    return render(request, 'index.html', {'name':html_table})


def inventory(request):
    if request.method == 'POST':
        form = Traking_forms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            serial_number = form.cleaned_data['serial_number']
            value = form.cleaned_data['value']
            new_inventory = Trackin(
                name = name,
                serial_number = serial_number,
                value = value,
            )
            new_inventory.save()
            return redirect('index')
    else:
        form = Traking_forms()
    return render(request, 'inventory.html', {'form':form})





