from django.shortcuts import render, redirect
from vehicle.forms import VehicleForm
from vehicle.models import Vehicle
# Create your views here.
def emp(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = VehicleForm()
    return render(request,'index.html',{'form':form})
def show(request):
    vehicles = Vehicle.objects.all()
    return render(request,"show.html", {'vehicles':vehicles})
def edit(request, id):
    vehicle = Vehicle.objects.get(id=id)
    return render(request,'edit.html', {'vehicle':vehicle})
def update(request, id):
    vehicle = Vehicle.objects.get(id=id)
    form = VehicleForm(request.POST, instance = vehicle)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'vehicle': vehicle})
def destroy(request, id):
    vehicle = Vehicle.objects.get(id=id)
    vehicle.delete()
    return redirect("/show")