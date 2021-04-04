from django.shortcuts import render, Http404, HttpResponseRedirect
from django.views.generic import View
from apps.main.models import ClanInfo
from apps.main.views import MainView
from .models import Article, Comment
# Create your views here.

class News(View):
    def get(self, request, *args, **kwargs):
        clan = ClanInfo.objects.get()
        articles = Article.objects.filter(is_publicate=True).order_by('-date')
        return render(request, "news/news.html", {'online': MainView.online(), 'clan': clan, 'articles': articles})

class Articles(View):
    def get(self, request, article_id, *args, **kwargs):
        try:
            article = Article.objects.get(id = article_id)  
        except:
            raise Http404("Статья не найдена") 

        clan = ClanInfo.objects.get()
        comments = Comment.objects.filter(article=article).order_by('-date').select_related()
        return render(request, 'news/article.html', {'online': MainView.online(), 'clan': clan,
                                                     'article': article, 'comments': comments})
    
    def post(self, request, article_id, *args, **kwargs):
        comment = Comment.objects.create(article = Article.objects.get(id = article_id),
                                         user=request.user,
                                         text=request.POST['text'])

        return HttpResponseRedirect(self.request.path_info)
