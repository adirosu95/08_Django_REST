from django.urls import path
from .views import articles_list, article_detail, ArticlesAPIView, ArticleDetails


urlpatterns = [
    # path('articles/', articles_list, name="articles"),
    # path('articles/<int:pk>/', article_detail, name="article_detail"),
    path('articles/', ArticlesAPIView.as_view(), name="articles"),
    path('articles/<int:pk>/', ArticleDetails.as_view(), name="article_details"),
]
