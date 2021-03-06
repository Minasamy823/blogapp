from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ArticleForm
from .models import *
from django.views.generic.edit import FormView


# Create your views here.
def ViewArticles(request):
    template_name = 'home.html'
    try:
        articles = Blog.objects.order_by('-published_at')[:10]
        super_article = Blog.objects.order_by('-published_at')[0]
    except IndexError:
        super_article, articles = None, None
    context = {'articles': articles, 'super_article': super_article}
    return render(request, template_name, context)


class PostArticles(FormView):
    template_name = 'post.html'
    form_class = ArticleForm
    success_url = 'home'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super(PostArticles, self).form_valid(form)
