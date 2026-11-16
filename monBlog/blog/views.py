from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import ArticleForm, CategorieForm
from .models import Article, Categorie

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
        type = self.request.GET.get('champ')
        if type:
            if type == 'nom':
                return Article.objects.filter(titre__icontains=query)
            if type == 'categorie':
                categories = Categorie.objects.filter(nom__icontains=query)
                return Article.objects.filter(categorie__in=categories)
            # if type == 'date':
            #     date = query.format("YYYY-MM-DD HH:MM")
            #     return Article.objects.filter(date_publication__gte=date)
            # print(type) 
            
        if query:
            return Article.objects.filter(titre__icontains=query).order_by("-date_publication")
        return Article.objects.all().order_by("-date_publication")


class ListeCategorieView(ListView):
    model = Categorie
    template_name = 'blog/liste_categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        "Trie les catégories par ordre alphabétique décroissant"
        articles = Categorie.objects.all().order_by("-nom")
        return articles


class CreerArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/creer_article.html'
    success_url = reverse_lazy('liste_articles') # redirection après création

class CreerCategorieView(CreateView):
    model = Categorie
    form_class = CategorieForm
    template_name = 'blog/creer_categorie.html'
    success_url = reverse_lazy('liste_categories')