from django.urls import path
from myapp.views import index, indexitem

app_name="myapp"
urlpatterns = [
    #http://127.0.0.1:8000/myapp/
    path('', index),
    #http://127.0.0.1:8000/myapp/hello/

    path('<int:my_id>/', indexitem, name="detail"),

    #http://127.0.0.1:8000/myapp/

]