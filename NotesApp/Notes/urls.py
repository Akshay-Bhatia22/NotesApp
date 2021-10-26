from django.urls import path
from . import views
from NotesApp.settings import DEBUG, STATIC_ROOT,STATIC_URL,MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static

app_name = "Notes"
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('collections/', views.collections, name='collections'),
    # path('update/<str:Notes_title>', views.update),
    path('detail/<str:Notes_title>/update', views.update),
    path('detail/<str:Notes_title>/delete', views.delete_note),
    path('detail/<str:Notes_title>', views.detail),

# -----------------------------------API------------------------------------------------
    path('api/',views.List_notes_all_create_api),
    path('api/detail/<str:Notes_title>/',views.Note_detail_api),

]

urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
