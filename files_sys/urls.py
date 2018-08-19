from django.conf.urls import url
from . import views
# from .apiviews import FileList

app_name = 'files_sys'

urlpatterns = [
    url(r'^$', views.filelist, name='list'),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
    url(r'^delete/(?P<pk>[\w]+)/$', views.delete_file, name='delete'),
    url(r"api/", views.file_list, name="api"),
]
