from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.ListCreate.as_view()),
    # path('student/',views.StudentCreate.as_view()),
    path('student/<int:pk>',views.UpdateRetrieveDestroy.as_view()),
    # path('student/<int:pk>',views.StudentUpdate.as_view()),
    # path('student/<int:pk>',views.StudentDestroy.as_view()),
   
]
