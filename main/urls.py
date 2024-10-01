from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "main"

urlpatterns = [
    path('', views.show_main, name="show_main"),
    path('xml/', views.show_xml, name="show_xml"),
    path('json/', views.show_json, name="show_json"),
    path('xml/<uuid:id>/', views.show_xml_by_id, name="show_xml_by_id"),
    path('json/<uuid:id>/', views.show_json_by_id, name="show_json_by_id"),
    path('registration/', views.registration, name="registration"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('add_product/', views.add_product, name="add_product"),
    path('edit_product/<uuid:id>/', views.edit_product, name="edit_product"),
    path('delete_product/<uuid:id>/', views.confirm_delete, name="confirm_delete"),
    path('delete/<uuid:id>/', views.delete_product, name="delete_product"),
    path('404/', views.page404, name='page404'),
    path('forgo-pasword/', views.forgot_password, name='forgot_password'),
    path('about/', views.about, name='about'),
    path('my-products/', views.show_my_products, name='my_products'),
]

# Hanya untuk development, supaya file media bisa diakses
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

