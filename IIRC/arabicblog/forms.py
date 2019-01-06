from django import forms
from django.utils import timezone
from django.utils.functional import curry
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from pinax.images.models import ImageSet

from .models import Post, Section

from tinymce.widgets import TinyMCE


FIELDS = [
    "section",
    "kateb",
    "title",
    "slug",
    "teaser",
    "content",
    "video",
    "description",
]


class PostFormMixin(object):

    def __init__(self, *args, **kwargs):
        super(PostFormMixin, self).__init__(*args, **kwargs)
        post = self.instance

    def save_post(self, post):
        post.updated = timezone.now()
        post.save()

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
    video = forms.CharField(
        label=_("Video"),
        widget=forms.Textarea(attrs={"style": "width: 80%;"}),
        required=False
    )
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
            "video",
            "description",

        ]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        if Section.objects.count() < 2:
            self.section = Section.objects.first()
            del self.fields["section"]
        else:
            self.section = None

    def save(self, blog=None, kateb=None):
        post = super(PostForm, self).save(commit=False)
        if blog:
            post.blog = blog
        if kateb:
            post.author = kateb
        if self.section:
            post.section = self.section
        post.slug = slugify(post.title)
        return self.save_post(post)
