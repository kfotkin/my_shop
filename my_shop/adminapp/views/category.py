from itertools import product
from django.shortcuts import get_object_or_404, render
from mainapp.models import ProductCategory
from adminapp.utils import superuser_required
from adminapp.forms import ProductCategotyAdminForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse


@superuser_required
def category_create(request):
    if request.method == "POST":
        form = ProductCategotyAdminForm(request.POST)    
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        form = ProductCategotyAdminForm()

    return render(
        request,
        "adminapp/category/edit.html",
        context={
            "title": "Создание категории",
            "form": form,
    },
)


@superuser_required
def categories(request):
    categories = ProductCategory.objects.all().order_by('id')

    return render(request, 'adminapp/category/categories.html', context={
        'title': 'Категории продуктов',
        'objects': categories
    })



@superuser_required
def category_update(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == "POST":
        form = ProductCategotyAdminForm(request.POST, instance=category)    
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        form = ProductCategotyAdminForm(instance=category)

    return render(
        request,
        "adminapp/category/edit.html",
        context={
            "title": "Создание категории",
            "form": form,
    },
)


@superuser_required
def category_delete(request, pk):
    title = 'Удаление категории'
    
    category = get_object_or_404(ProductCategory, pk=pk)
    
    if request.method == 'POST':
        #user.delete()
        #вместо удаления лучше сделаем неактивным
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('admin:categories'))

    content = {'title': title, 'category_to_delete': category}
    
    return render(request, 'adminapp/category/delete.html', content)
