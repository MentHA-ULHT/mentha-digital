from django.urls import path
from . import views


app_name = 'mentha'

urlpatterns = [
    path('',views.index_page_view, name='index'),
    path('parceiros/', views.parceiros_page_view, name='parceiros'),
    path('aplicacoes/', views.aplicacoes_page_view, name='aplicacoes'),
    path('projeto/', views.projeto_page_view, name='projeto'),
    path('mentha-cog/', views.mentha_cog_page_view, name='mentha-cog'),
    path('contacto/', views.contacto_page_view, name='contacto'),
    path('home/',views.home_page_view, name='home'),
    path('noticias/',views.noticias_page_view, name='noticias'),
    path('videoconferencia/',views.videoconferencia_page_view, name='videoconferencia'),
    path('login/',views.login_page_view, name='login'),
    path('logout/',views.logout_page_view, name='logout'),
]