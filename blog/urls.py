from django.urls import path, include
from .views import PostsView, PostsDetailsView

urlpatterns = [
    path('', PostsView.as_view()),
    path('<int:postID>', PostsDetailsView.as_view()),
]
