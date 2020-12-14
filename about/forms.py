# coding:utf8

from django import forms
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from ckeditor.widgets import CKEditorWidget

from .models import AboutPost


class AboutPostAdminForm(forms.ModelForm):
    body = forms.CharField(
        label=_("content"),
        widget=CKEditorWidget()
    )

    class Meta:
        model = AboutPost
        fields = []

    def save(self, commit=True):
        post = super(AboutPostAdminForm, self).save(commit=False)

        if post.pk is None or AboutPost.objects.filter(pk=post.pk, publish_time=None).count():
            if self.cleaned_data["state"] == 1:
                post.publish_time = now()

        post.body = self.cleaned_data["body"]
        post.update_time = now()
        post.save()

        return post
