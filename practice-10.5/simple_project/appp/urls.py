from django.urls import path, include
from . import views
urlpatterns = [
    path('about/', views.about),
    # path('simple_project/', include('simple_project.urls')),
]
