from django.urls import path

from . import views

app_name = "todo"

urlpatterns = [
    path(
        "todos",
        views.TodoViewSet.as_view({"get": "list", "post": "create"}),
        name="todos",
    ),
]
