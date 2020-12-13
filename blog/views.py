# coding:utf8

from django.db.models import Q
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, DateDetailView
from django.http import Http404
from random import shuffle
from blog.models import BlogPost
from labels.models import YmeLabel


class BlogIndexView(ListView):
    model = BlogPost
    template_name = "blog/blog_list.html"
    search_parm = "q"
    paginate_by = settings.POST_PAGINATE_BY

    def get_search_term(self):
        return self.request.GET.get(self.search_parm)

    def get_current_labels(self):
        labels = list(YmeLabel.objects.current())
        shuffle(labels)
        return labels

    def get_context_data(self, **kwargs):
        context = super(BlogIndexView, self).get_context_data(**kwargs)
        context.update({
            "labels_list": self.get_current_labels(),
            "search_term": self.get_search_term(),
        })
        return context

    def search(self, posts):
        q = self.get_search_term()
        if q:
            posts = posts.filter(
                Q(title__icontains=q) |
                Q(teaser__icontains=q) |
                Q(body__icontains=q)
            )
        return posts

    def get_queryset(self):
        return self.search(BlogPost.objects.current())


class BlogDetailView(DetailView):
    model = BlogPost
    pk_url_kwarg = "post_pk"
    template_name = "blog/blog_post.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated() and not request.user.is_staff:
            raise Http404
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class BlogDetailAdminView(DetailView):
    model = BlogPost
    slug_url_kwarg = "post_secret_key"
    slug_field = "secret_key"
    template_name = "blog/blog_post.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_published:
            return redirect(self.object.get_absolute_url())
        else:
            return super(BlogDetailAdminView, self).get(request, *args, **kwargs)


class DateBasePostDetailView(DateDetailView):
    model = BlogPost
    month_format = "%m"
    date_field = "publish_time"
    template_name = "blog/blog_post.html"

    def get_current_labels(self):
        labels = list(YmeLabel.objects.current())
        shuffle(labels)
        return labels

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context.update({"labels_list": self.get_current_labels(), })
        return self.render_to_response(context)

    def get_queryset(self):
        queryset = super(DateBasePostDetailView, self).get_queryset()
        queryset = queryset.filter(state=1)
        return queryset
