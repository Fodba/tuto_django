from django.urls import path
from . import views
from .views import ListeArticlesView, CreerArticleView

urlpatterns = [
    # path('',views.liste_articles,name="liste_articles"),
    path('', ListeArticlesView.as_view(), name='liste_articles'),
    path('nouveau/',CreerArticleView.as_view(), name="creer_article")
]