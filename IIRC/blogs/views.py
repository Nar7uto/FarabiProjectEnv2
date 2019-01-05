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
    posts = blog_post.objects.all().order_by('-published')[0:5]
    mainSlide = blog_post.objects.all().order_by('-published')[0]
    otherSlides = blog_post.objects.all().order_by('-published')[1:4]
    newsPosts = blog_post.objects.filter(section_id='1').order_by('-published')[0:3]
    lastNewsPost = blog_post.objects.filter(section_id='1').order_by('-published')[0]
    articles = blog_post.objects.filter(section_id='2').order_by('-published')[0:4]
    lastArticle = blog_post.objects.filter(section_id='2').order_by('-published')[0]
    reports = blog_post.objects.filter(section_id='3').order_by('-published')[0:3]
    lastReport = blog_post.objects.filter(section_id='3').order_by('-published')[0]
    images = blog_post.objects.filter(section_id='6').order_by('-published')[0:4]
    allImages = blog_post.objects.filter(section_id='6').order_by('-published')
    lastImage = allImages[0]
    image2= allImages[1]
    image3= allImages[2]
    image4= allImages[2]

    videos = blog_post.objects.filter(section_id='8').order_by('-published')[0:3]
    lastVideo = blog_post.objects.filter(section_id='8').order_by('-published')[0]

    context = {
        'main': mainSlide,
        'other': otherSlides,
        'posts': posts,
        'news': newsPosts,
        'lastNews': lastNewsPost,
        'articles': articles,
        'lastArticle': lastArticle,
        'reports': reports,
        'lastReport': lastReport,
        'images': images,
        'lastImage': lastImage,
        'videos': videos,
        'lastVideo': lastVideo,
        'image1': lastImage,
        'image2': image2,
        'image3': image3,
        'image4': image4,

    }
    return render(request, 'site_base.html', context)

