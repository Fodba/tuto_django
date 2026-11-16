from django.urls import path
from . import views
from .views import ListeArticlesView, CreerArticleView, ListeCategorieView, CreerCategorieView

urlpatterns = [
    # path('',views.liste_articles,name="liste_articles"),
    path('articles', ListeArticlesView.as_view(), name='liste_articles'),
    path('articles/nouveau/',CreerArticleView.as_view(), name="creer_article"),
    path('categories', ListeCategorieView.as_view(), name='liste_categories'),
    path('categories/nouveau/',CreerCategorieView.as_view(), name="creer_categorie"),
]