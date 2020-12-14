# coding:utf8

from django.shortcuts import render, redirect
from django.views.generic import DetailView
from random import shuffle

from labels.models import YmeLabel
from .models import AboutPost


# Create your views here.
def about_view(request):
    labels = list(YmeLabel.objects.current())
    shuffle(labels)
    return render(request, "about.html", context={"labels_list": labels})


class AboutView(DetailView):
    model = AboutPost
    template_name = "about.html"
    search_parm = "q"

    def get_search_term(self):
        return self.request.GET.get(self.search_parm)

    def get_current_labels(self):
        labels = list(YmeLabel.objects.current())
        shuffle(labels)
        return labels

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context.update({
            "labels_list": self.get_current_labels(),
            "search_term": self.get_search_term(),
        })
        return context

    def get(self, request, *args, **kwargs):
        qs = AboutPost.objects.filter(state=1)
        self.object = None if not qs else qs.latest("publish_time")
        return self.render_to_response(
            self.get_context_data(object=self.object)
        )


class AboutAdminView(DetailView):
    model = AboutPost
    slug_url_kwarg = "post_secret_key"
    slug_field = "secret_key"
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.is_published:
            return super(AboutAdminView, self).get(request, *args, **kwargs)
        else:
            return redirect(self.object.get_absolute_url())
