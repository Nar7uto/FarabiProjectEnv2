from django.shortcuts import render
from .form import SignUpForm
from .form import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Post
from pinax.blog.models import Post as blog_post

def blogs(request):
    # return render(request, 'base.html', {})
    return render(request, 'landing.html', {})


def homepage(request):
    return render(request, 'homepage.html', {})


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
    # return render(request, 'base.html', context)
    return render(request, 'index.html', context)


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
    return render(request, 'contact-us.html', context)


class Postclass():
    class Meta:
        model = Post
        fields = ['email', 'fullname']


def post(request):
    new_post = Post.objects.all()[:1]
    context = {
        'show_post': new_post
    }
    return render(request, 'test.html', context)


def home(request):
    return render(request, 'home.html', {})


def arHome(request):
    return render(request, 'snippet/arHome.html', {})


def en(request):
    title = "Welcome guest"
    posts = blog_post.objects.all().order_by('-published')[0:3]
    lastPost = posts[0]
    secondLastPost = posts[1]
    thirdLastPost = posts[2]
    newsPosts = blog_post.objects.filter(section_id='1').order_by('-published')[0:3]
    articles = blog_post.objects.filter(section_id='1').order_by('-published')[0:3]
    reports = blog_post.objects.filter(section_id='1').order_by('-published')[0:3]
    images = blog_post.objects.filter(section_id='1').order_by('-published')[0:3]
    videos = blog_post.objects.filter(section_id='1').order_by('-published')[0:3]

    context = {
        'posts': posts,
        '1st': lastPost,
        '2nd': secondLastPost,
        '3rd': thirdLastPost,
        'news': newsPosts,
    }
    return render(request, 'site_base.html', context)

