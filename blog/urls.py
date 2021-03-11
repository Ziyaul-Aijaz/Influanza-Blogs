from django.urls import path
from . import views 
from .views import AddPostView,DeletePost,CategoryView
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about',views.about, name='blog-about'),
#    path('add_post/',views.add_post,name='add_post')
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('article/<int:id>',views.detail_view,name='article_detail'),
    path('update/<int:id>',views.update_view,name='update_view'),
    path('article/<int:pk>/remove',DeletePost.as_view(),name='remove_post'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('categories',views.category_home,name='category_home'),
    #path('like/<int:pk>', views.LikeView, name='like_post'),
    #path('auhtor/<int:author_id>/', views.AuthorDetail,name='author_detail')
]