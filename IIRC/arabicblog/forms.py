from django import forms
from django.utils import timezone
from django.utils.functional import curry
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from pinax.images.models import ImageSet

from .conf import settings
from .models import Post, Section
from .signals import post_published
from .utils import load_path_attr

from tinymce.widgets import TinyMCE


FIELDS = [
    "section",
    "author",
    "title",
    "slug",
    "teaser",
    "content",
    "description",
    "state"
]


class PostFormMixin(object):

    def __init__(self, *args, **kwargs):
        super(PostFormMixin, self).__init__(*args, **kwargs)
        post = self.instance

    def save_post(self, post):
        published = False

        if post.pk is None or Post.objects.filter(pk=post.pk, published=None).count():
            if self.cleaned_data["state"] == Post.STATE_CHOICES[-1][0]:
                post.published = timezone.now()
                published = True

        post.updated = timezone.now()
        post.save()

        if published:
            post_published.send(sender=Post, post=post)

        return post


class AdminPostForm(PostFormMixin, forms.ModelForm):

    title = forms.CharField(
        label=_("Title"),
        max_length=90,
        widget=forms.TextInput(attrs={"style": "width: 50%;"}),
    )
    slug = forms.CharField(
        label=_("Slug"),
        widget=forms.TextInput(attrs={"style": "width: 50%;"})
    )
    teaser = forms.CharField(
        label=_("Teaser"),
        widget=forms.Textarea(attrs={"style": "width: 80%;"}),
    )
    content = forms.CharField(
        widget=TinyMCE(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        ))

    description = forms.CharField(
        label=_("Description"),
        widget=forms.Textarea(attrs={"style": "width: 80%;"}),
        required=False
    )

    class Meta:
        model = Post
        fields = '__all__'
        # fields = FIELDS

    def save(self, blog=None):
        post = super(AdminPostForm, self).save(commit=False)
        if blog:
            post.blog = blog
        return self.save_post(post)


class PostForm(PostFormMixin, forms.ModelForm):

    teaser = forms.CharField(widget=forms.Textarea())
    content = forms.CharField(
        widget=TinyMCE(
            attrs={'required': False, 'cols': 30, 'rows': 10}))
    class Meta:
        model = Post
        fields = [
            "section",
            "title",
            "teaser",
            "content",
            "description",
            "state"
        ]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        if Section.objects.count() < 2:
            self.section = Section.objects.first()
            del self.fields["section"]
        else:
            self.section = None

    def save(self, blog=None, author=None):
        post = super(PostForm, self).save(commit=False)
        if blog:
            post.blog = blog
        if author:
            post.author = author
            post.image_set = ImageSet.objects.create(created_by=author)
        if self.section:
            post.section = self.section
        post.slug = slugify(post.title)
        return self.save_post(post)