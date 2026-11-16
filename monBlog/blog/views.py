from django.shortcuts import render
from django.views.generic import ListView
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

    def get_queryset(self):
        "Trie les articles par ordre alphabétique décroissant"
        articles = Article.objects.all().order_by("-titre")
        return articles

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Article.objects.filter(titre__icontains=query)
        return Article.objects.all()