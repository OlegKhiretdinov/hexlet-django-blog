from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from hexlet_django_blog.article.models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })

class ArticleView(View):
    def get(self, request, tag, article_id,  *args, **kwargs):
        # return HttpResponse('Hello, World!')

        return render(request, 'articles/article.html', context={
                'title': 'Articles',
                'article_id': article_id,
                'tag': tag,
            })

