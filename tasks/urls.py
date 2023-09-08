from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:task_id>/", views.detail, name="detail"),
    path("<int:task_id>/", views.delete_task, name="delete"),
    path("new_task", views.new_task, name="create_task"),
    path("history", views.history, name="history")
]