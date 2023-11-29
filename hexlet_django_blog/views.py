from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.urls import reverse


def index(request):
    # return render(request, 'article.html', context={
    #     'who': 'World',
    # })
    return redirect(reverse('article', kwargs={'article_id': 42, 'tag': 'python'}), permanent=True,)


class HomePageView(TemplateView):
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context

    def get(self, request, *args, **kwargs):
        return redirect(
            reverse('article', kwargs={'article_id': 42, 'tag': 'python'}),
            permanent=True,
        )


def about(request):
    return render(request, 'about.html')
