from re import template
from django.shortcuts import render, get_object_or_404
from authapp.models import ShopUser
from adminapp.utils import superuser_required
from adminapp.forms import ShopUserCreateAdminForm, ShopUserEditAdminForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from django.utils.decorators import method_decorator


class UserListView(ListView):
    model = ShopUser
    template_name = 'adminapp/user/users.html'
    paginate_by = 1

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список пользователей'
        return context


class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user/edit.html'
    form_class = ShopUserCreateAdminForm
    success_url = reverse_lazy("admin:users")

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание пользователя'
        return context


class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user/edit.html'
    form_class = ShopUserEditAdminForm
    success_url = reverse_lazy("admin:users")

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Редактирование пользователя"
        return context


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user/delete.html'
    success_url = reverse_lazy("admin:users")   

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление пользователя'
        return context

    # def get_object(self, queryset):
    #     return queryset.get(pk=self.kwargs.get('pk'))


# @superuser_required
# def user_create(request):
#     if request.method == "POST":
#         edit_form = ShopUserAdminForm(request.POST, request.FILES)    
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin:users'))
#     else:
#         edit_form = ShopUserAdminForm()

#     return render(
#         request,
#         "adminapp/user/edit.html",
#         context={
#             "title": "Создание пользователя",
#             "form": edit_form,
#     },
# )


# @superuser_required
# def users(request):
#     users = ShopUser.objects.all().order_by('id')

#     return render(request, 'adminapp/user/users.html', context={
#         'title': 'Пользователи',
#         'objects': users
#     })


# @superuser_required
# def user_update(request, pk):
#     user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == "POST":
#         edit_form = ShopUserAdminForm(request.POST, request.FILES, instance=user)    
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin:users'))
#     else:
#         edit_form = ShopUserAdminForm(instance=user)

#     return render(
#         request,
#         "adminapp/user/edit.html",
#         context={
#             "title": "Редактирование пользователя",
#             "form": edit_form,
#     },
# )


# @superuser_required
# def user_delete(request, pk):
#     title = 'Удаление пользователя'
    
#     user = get_object_or_404(ShopUser, pk=pk)
    
#     if request.method == 'POST':
#         #user.delete()
#         #вместо удаления лучше сделаем неактивным
#         user.is_active = False
#         user.save()
#         return HttpResponseRedirect(reverse('admin:users'))

#     content = {'title': title, 'user_to_delete': user}
    
#     return render(request, 'adminapp/user/delete.html', content)

