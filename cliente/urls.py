from django.urls import path
from .views import principal, cadastrar_cliente, consultar_cliente, editar_cliente

app_name = 'cliente'

urlpatterns = [
    path('', principal, name='principal'),
    path('cadastrar/', cadastrar_cliente, name='cadastrar'),
    path('consultar/', consultar_cliente, name='consultar'),
    path('consultar/<int:id>/update/', editar_cliente, name='update'),
]