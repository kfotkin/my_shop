from itertools import product
from django.shortcuts import get_object_or_404, render
from mainapp.models import ProductCategory
from adminapp.utils import superuser_required
from adminapp.forms import ProductCategotyAdminForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import DeleteView
from django.urls import reverse, reverse_lazy


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

# class ProductCategoryDeleteView(DeleteView):
#     model = ProductCategory
#     template_name = 'adminapp/category/delete.html'
#     success_url = reverse_lazy('admin:categories')
    
#     def delete(self, request, *args, **kwargs):
#         success_url = self.get_success_url()
#         self.object = self.get_object()
#         self.object.is_active = False
#         self.object.save()
#         return HttpResponseRedirect(success_url)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Удаление категории'
#         return context
