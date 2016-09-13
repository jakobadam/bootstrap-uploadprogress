from django import shortcuts
from django import http

from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from .models import Package
from .forms import PackageForm

def package_list(request):
    return shortcuts.render(request, 'package_list.html', {
        'packages': Package.objects.all()
    })

def package_add(request, instance=None):
    status = 200
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            instance = form.save()
            messages.success(request, u'{} uploaded'.format(instance))
            return http.HttpResponseRedirect(reverse('package_list'))
        else:
            status = 422
    else:
        form = PackageForm(instance=instance)

    return shortcuts.render(request, 'package_form.html', {
        'form':form
    }, status=status)

def package_edit(request, pk):
    package = shortcuts.get_object_or_404(Package, pk=pk)
    return package_add(request, instance=package)

@require_http_methods(['POST'])
def package_delete(request, pk):
    package = shortcuts.get_object_or_404(Package, pk=pk)
    package.delete()
    messages.info(request, 'Deleted {}'.format(package))
    return http.HttpResponseRedirect(reverse('package_list'))

