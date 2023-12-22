from django.shortcuts import render, get_object_or_404, redirect
from .models import Property,Tenant,Unit
from .forms import PropertyForm,TenantForm

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})

def edit_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'edit_property.html', {'form': form})

def delete_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        property.delete()
        return redirect('property_list')
    return render(request, 'delete_property.html', {'property': property})



def tenant_profile(request, tenant_id):
    tenant = Tenant.objects.get(id=tenant_id)
    return render(request, 'tenant_profile.html', {'tenant': tenant})

def assign_tenant(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('tenant_profile')
    else:
        form = TenantForm()
    return render(request, 'assign_tenant.html', {'form': form})


def search(request):
    if request.method == 'GET':
        property_features = request.GET.get('property_features')
        unit_features = request.GET.get('unit_features')

        properties = Property.objects.filter(features__icontains=property_features)
        units = Unit.objects.filter(features__icontains=unit_features)

        context = {
            'properties': properties,
            'units': units,
        }
        return render(request, 'search_results.html', context)

    return render(request, 'search_form.html')
