# from django.urls import path

# from cats.views import cat_list

# urlpatterns = [
#    path('cats/', cat_list),
# ]


# ----------


# # urls.py
# from django.urls import path

# from cats.views import APICat, APICatDetail

# urlpatterns = [
#     path('cats/', APICat.as_view()),
#     path('cats/<int:pk>', APICatDetail.as_view()),
# ]


# ----------


# Обновлённый urls.py
from django.urls import path

from cats.views import CatList, CatDetail

urlpatterns = [
    path('cats/', CatList.as_view()),
    path('cats/<int:pk>/', CatDetail.as_view()),
]


