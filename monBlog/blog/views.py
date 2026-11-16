from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import ArticleForm
from .models import Article

# Create your views here.
def liste_articles(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(
        request=request,
        template_name='blog/liste_articles.html',
        context=context
    )

class ListeArticlesView(ListView):
    model = Article
    template_name = 'blog/liste_articles.html'
    context_object_name = 'articles'

    # def get_queryset(self):
    #     "Trie les articles par ordre alphabétique décroissant"
    #     articles = Article.objects.all().order_by("-titre")
    #     return articles

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Article.objects.filter(titre__icontains=query).order_by("-date_publication")
        return Article.objects.all().order_by("-date_publication")

class CreerArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/creer_article.html'
    success_url = reverse_lazy('liste_articles') # redirection après création
    