from rest_framework import routers
from . import viewset

router = routers.DefaultRouter()

router.register("", viewset.ProjetViewset, basename="Projet_python_Django")
urlpatterns = router.urls
