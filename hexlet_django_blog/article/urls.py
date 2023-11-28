from django.urls import path
from hexlet_django_blog.article import views

urlpatterns = [
    path(
        '<str:tag>/<int:article_id>',
        views.ArticlesListView.as_view(),
        name='article'
    ),
]
