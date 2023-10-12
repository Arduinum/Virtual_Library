from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import SignInForm, EditUserForm
from django.views.generic import FormView
from django.views import View


class SignInView(FormView):
    form_class = SignInForm
    template_name = 'accounts/sign_in.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        remember_me = form.cleaned_data['remember_me']
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            if not remember_me:
                self.request.session.set_expiry(0)
            return redirect('library:books')
        form.add_error(None, 'Неверный логин или пароль!')
        return self.form_invalid(form)


class CreateUserView(FormView):
    form_class = EditUserForm
    template_name = 'accounts/user_edit.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = form.cleaned_data['username']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('accounts:sign_in')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    

class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('accounts:sign_in')
