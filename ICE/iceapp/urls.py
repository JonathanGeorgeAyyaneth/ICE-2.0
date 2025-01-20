from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import set_language

urlpatterns = [
    path('i18n/setlang/', set_language, name='set_language'),
    path('person/<int:pk>/', views.person_detail, name='person_detail'),
    path('institution_building/<int:pk>/', views.institution_building_detail, name='institution_building_detail'),
    path('church_and_other_building/<int:pk>/', views.church_and_other_building_detail, name='church_and_other_building_detail'),
    path('major_celebration_historical_event/<int:pk>/', views.major_celebration_historical_event_detail, name='major_celebration_historical_event_detail'),
    path('church_community/<int:pk>/', views.church_community_detail, name='church_community_detail'),
    path('search_suggestions/', views.search_suggestions, name='search_suggestions'),
    path('search_results/', views.search_results, name='search_results'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name="login"),
    path('login_view/', views.login_view, name="login_view"),
    path('signup/', views.signup, name="signup"),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),

    path('2index/', views.new_index, name='2index'),
    path('category/<str:category_name>/', views.category_view, name='category_view'),
    
    path('like_or_dislike/<str:model_name>/<int:object_id>/<str:action>/', views.like_or_dislike, name='like_or_dislike'),
    path('load_comments/<str:model_name>/<int:object_id>/<int:offset>/', views.load_comments, name='load_comments'),
    path('add_comment/<int:content_type_id>/<int:object_id>/', views.add_comment, name='add_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    # path('verify_otp/', views.mfa,name='verify_otp'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),


]
