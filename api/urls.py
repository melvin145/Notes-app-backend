from django.urls import path
from .views import *;

urlpatterns=[
    path("",getRoutes,name="routes"),
    path("notes",getNotes,name="notes"),
    path("notes/<str:pk>/update",updateNote,name="update"),
    path("notes/<str:pk>/delete",deleteNote,name="delete"),
    path("notes/new",addNote,name="add"),
    path("notes/<str:pk>",getNote,name="notes"),
]
