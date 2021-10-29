from django.db import models
from django.contrib.auth import get_user_model
from common.models import Base


class Projet(Base):
    name = models.CharField(max_length=80, null=True)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="Projet_python_Django"
    )

    def __str__(self):
        return self.name