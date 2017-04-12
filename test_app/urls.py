from django.conf.urls import url
from views import ArticleDetailView, ArticleListView

urlpatterns = [
    url(r'^article/list/(?P<pk>[0-9]+)/$', ArticleDetailView, name='article-detail'),
    url(r'^$', ArticleListView, name='article-list'),
]
