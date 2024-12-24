from django.urls import path
from . import views

urlpatterns = [
    path('', views.nueva_pagina, name='inicio'),
    path('login/', views.login_view, name='login'),  # Página de inicio de sesión
    path('home/', views.home_view, name='home'),  # Página principal
    path('eventos/', views.containers_view, name='eventos'),  # Contenedores
    path('logout/', views.logout_view, name='logout'),  # Nueva ruta para logout
    path('register/', views.register_view, name='register'),  # Nueva ruta para registro
    path('users/', views.user_list_view, name='user_list'),
    path('login/', views.login_view, name='login'),
    path('lugares/', views.lista_lugares, name='lista_lugares'),
    path('lugares/agregar/', views.agregar_lugar_usuario, name='agregar_lugar_usuario'),
    path('panel-admin/lugares/', views.admin_lista_lugares, name='admin_lista_lugares'),  # Panel admin para ver lugares
    path('panel-admin/lugares/agregar/', views.agregar_lugar_admin, name='agregar_lugar_admin'),
    path('panel-admin/lugares/editar/<int:lugar_id>/', views.editar_lugar, name='editar_lugar'),
    path('panel-admin/lugares/eliminar/<int:lugar_id>/', views.eliminar_lugar, name='eliminar_lugar'), # Eliminar lugar (admin)
    path('nueva_pagina/', views.nueva_pagina, name = 'nueva_pagina'),
    path('contact/', views.contact, name='contacto'),
    path('usuarios/editar/<int:user_id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),

]


