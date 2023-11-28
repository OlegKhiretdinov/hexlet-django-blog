from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# def index(request):
#     return render(request, 'articles/index.html', context={
#         'title': 'Articles',
#     })


class ArticlesListView(View):

    def get(self, request, tag, article_id,  *args, **kwargs):
        # return HttpResponse('Hello, World!')

        return render(request, 'articles/index.html', context={
                'title': 'Articles',
                'article_id': article_id,
                'tag': tag,
            })

