from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register('background-disease', views.BackgroundDiseaseAPI, basename='background-disease')
router.register('symptom', views.SymptomAPI, basename='symptom')
router.register('medical-declaration', views.MedicalDeclarationAPI, basename='medical-declaration')
router.register('test', views.TestAPI, basename='test')
router.register('vaccine', views.VaccineAPI, basename='vaccine')

urlpatterns = router.urls