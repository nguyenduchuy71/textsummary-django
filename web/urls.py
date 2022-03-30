from django.urls import path
from .views import SummaryView, index, ViewUploadFile

app_name = 'web'

urlpatterns = [
    path(r'', index, name='index'),
    path(r'summary/', SummaryView.as_view(), name='summary'),
    path(r'upload/', ViewUploadFile.as_view(), name='upload'),
]
