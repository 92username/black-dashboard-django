# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Modelo de funcionário

class Employee(models.Model):
    name = models.CharField(max_length=100)  # Nome do funcionário
    email = models.EmailField(unique=True)  # E-mail único
    age = models.IntegerField()  # Idade
    position = models.CharField(max_length=50)  # Cargo
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação

    def __str__(self):
        return self.name  # Mostra o nome ao referenciar o objeto
    
    
