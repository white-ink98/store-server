from django.shortcuts import HttpResponseRedirect
from django.contrib import auth
# from django.contrib.auth.decorators import login_required

from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket
from mymixin.views import TitleMixin


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Store- Авторизація'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Ви успішно зареєстровані!'
    title = 'Store- Реєстрація'

    # def get_context_data(self, **kwargs):
    #     context = super(UserRegistrationView, self).get_context_data()
    #     context["title"] = 'Store- Реєстрація'
    #     return context


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store- Аккаунт'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context["baskets"] = Basket.objects.filter(user=self.object)
        return context


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

# def login(request):
#    if request.method == 'POST':
#        form = UserLoginForm(data=request.POST)
#        if form.is_valid():
#            username = request.POST['username']
#            password = request.POST['password']
#            user = auth.authenticate(username=username, password=password)
#            if user:
#                auth.login(request, user)
#                return HttpResponseRedirect(reverse('index'))
#    else:
#        form = UserLoginForm()
#    context = {'form': form}
#    return render(request, 'users/login.html', context)


# def registration(request):
#    if request.method == 'POST':
#        form = UserRegistrationForm(data=request.POST)
#        if form.is_valid():
#            form.save()
#            messages.success(request, 'Ви успішно зареєстровані!')
#            return HttpResponseRedirect(reverse('users:login'))
#    else:
#        form = UserRegistrationForm()
#    context = {'form': form}
#    return render(request, 'users/registration.html', context)


# @login_required
# def profile(request):
#    if request.method == 'POST':
#        form = UserProfileForm(instance=request.user,
#                               data=request.POST, files=request.FILES)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect(reverse('users:profile'))
#    else:
#        form = UserProfileForm(instance=request.user)
#
#    context = {
#        'title': 'Store - Профіль',
#        'form': form,
#        'baskets': Basket.objects.filter(user=request.user),
#           # 'total_sum': sum(basket.sum() for basket in baskets),
#           # 'total_quantity': sum(basket.quantity for basket in baskets),
#    }
#    return render(request, 'users/profile.html', context)
