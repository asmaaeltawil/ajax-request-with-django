from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse
class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm

def validate_username(request): 
    username = request.GET.get('username')
    is_taken = User.objects.filter(username__iexact=username).exists()
    data = {'is_taken':is_taken}
    if data['is_taken']: 
        data['error_message'] = "The username already taken"
    return JsonResponse(data)