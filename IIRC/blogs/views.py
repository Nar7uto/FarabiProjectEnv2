from django.shortcuts import render
from .form import SignUpForm
from .form import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Post

def home(request):
    # return render(request, 'base.html', {})
    return render(request, 'homenew.html', {})


def land(request):
    return render(request, 'landing.html', {})


def index(request):
    title = "Welcome guest"
    form = SignUpForm(request.POST or None)
    if request.user.is_authenticated:
        title = "Welcome %s" % (request.user)
    context = {
        'title': title,
        'myName': 'Hasan',
        'form': form,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.fullname:
            email_base, provider = instance.email.split('@')
            instance.fullname = email_base
            instance.save()
        context = {
            'title': 'Thank for Registeration',
        }
    return render(request, 'base.html', context)
    # return render(request, 'index.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_fullname = form.cleaned_data.get('fullname')

        subject = 'Mail from Django'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'hasanshah5882@gmail.com']
        contact_message = '%s: %s via %s'%(
            form_fullname,
            form_message,
            form_email)
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)

    context = {
        'form': form,
    }
    return render(request, 'forms.html', context)


class Postclass():
    class Meta:
        model = Post
        fields = ['email', 'fullname']


def post(request):

    return render(request, 'home.html', {})

