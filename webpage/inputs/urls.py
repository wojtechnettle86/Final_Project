from django.urls import path
from .views import InputListView, InputCreateView, DetailView, InputUpdateView, InputDeleteView, Input, input_created

urlpatterns = [
    path("", InputListView.as_view(), name="inputs_list"),
    path("create/", InputCreateView.as_view(), name="input_create"),
    path("create/success/", input_created, name="input_created"),
    path("update/<int:pk>/", InputUpdateView.as_view(), name="input_update"),
    path("delete/<int:pk>/", InputDeleteView.as_view(), name="input_delete"),
    path("<int:pk>/", DetailView.as_view(template_name="inputs_detail.html", model=Input), name="inputs_detail"),
]