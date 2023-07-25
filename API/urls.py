from django.urls import path
from API.views import testView
    
urlpatterns = [
    
    path('user-details/',testView.as_view()),


]