from django.urls import path
from . import views
from NotesApp.settings import DEBUG, STATIC_ROOT,STATIC_URL,MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static

app_name = "Notes"
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    # path('update/<str:Notes_title>', views.update),
    path('detail/<str:Notes_title>/update', views.update),
    path('detail/<str:Notes_title>/delete', views.delete_note),
    path('detail/<str:Notes_title>', views.detail),
]

urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
