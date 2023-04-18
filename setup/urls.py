from django.contrib import admin
from django.urls import path, include
from empresa.views import DepartamentoViewSet, FuncionarioViewSet, ProjetoViewSet, ListaFuncionariosDepartamento, ListaProjetosDepartamento
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="CAM - Empresa API",
      default_version='v1',
      description="Sistema de gerenciamento de departamentos, funcionarios e projetos",
      terms_of_service="#",
      contact=openapi.Contact(email="pedroltdias@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('departamentos', DepartamentoViewSet, basename='Departamentos')
router.register('funcionarios', FuncionarioViewSet, basename='Funcionarios')
router.register('projetos', ProjetoViewSet, basename='Projetos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('departamento/<int:pk>/funcionarios/', ListaFuncionariosDepartamento.as_view()),
    path('departamento/<int:pk>/projetos/', ListaProjetosDepartamento.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
