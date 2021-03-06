# coding:utf8

from django import forms
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from ckeditor.widgets import CKEditorWidget

from .models import FotoPost


class FotoPostAdminForm(forms.ModelForm):
    title = forms.CharField(
        label=_("title"),
        max_length=90,
        widget=forms.TextInput(attrs={"style": "width: 50%;"}),
    )
    slug = forms.CharField(
        label=_("slug"),
        widget=forms.TextInput(attrs={"style": "width: 50%;"})
    )
    teaser = forms.CharField(
        label=_("teaser"),
        widget=CKEditorWidget(),
    )
    body = forms.CharField(
        label=_("content"),
        widget=CKEditorWidget()
    )

    class Meta:
        model = FotoPost
        fields = []

    def save(self, commit=True):
        post = super(FotoPostAdminForm, self).save(commit=False)

        if post.pk is None or FotoPost.objects.filter(pk=post.pk, publish_time=None).count():
            if self.cleaned_data["state"] == 1:
                post.publish_time = now()

        post.teaser = self.cleaned_data["teaser"]
        post.body = self.cleaned_data["body"]
        post.update_time = now()
        post.save()

        return post
