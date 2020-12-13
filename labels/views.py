# coding:utf8

from random import shuffle
from django.db.models import Q
from django.conf import settings
from django.views.generic import ListView

from blog.models import BlogPost
from foto.models import FotoPost
from .models import YmeLabel


class LabelIndexView(ListView):
    context_object_name = "home_list"
    template_name = "home.html"
    search_parm = "q"
    paginate_by = settings.POST_PAGINATE_BY

    def get_search_term(self):
        return self.request.GET.get(self.search_parm)

    def get_current_labels(self):
        labels = list(YmeLabel.objects.current())
        shuffle(labels)
        return labels

    def get_context_data(self, **kwargs):
        context = super(LabelIndexView, self).get_context_data(**kwargs)
        context.update({
            "labels_list": self.get_current_labels(),
            "search_term": self.get_search_term(),
        })
        return context

    def search(self, q, posts):
        posts = posts.filter(
            Q(title__icontains=q) |
            Q(teaser__icontains=q) |
            Q(body__icontains=q)
        )
        return posts

    def get_queryset(self):
        blog_list = BlogPost.objects.current().filter(
            labels__slug__exact=self.kwargs.get("label")
        )
        foto_list = FotoPost.objects.current().filter(
            labels__slug__exact=self.kwargs.get("label")
        )

        q = self.get_search_term()
        if q:
            blog_list = self.search(q, blog_list)
            foto_list = self.search(q, foto_list)
        return sorted(list(blog_list) + list(foto_list),
                      key=lambda x: x.publish_time, reverse=True)
