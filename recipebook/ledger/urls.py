from django.urls import path
from . import views

urlpatterns = [
    path('recipe/list/', views.recipe_list, name='recipe-list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe-detail'),
    path('recipe/add/', views.recipe_add, name='recipe-add'),
    path('recipe/<int:pk>/add_image/', views.recipe_add_image, name='recipe-add-image')
]

app_name = "ledger"