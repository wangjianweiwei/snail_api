# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2024/8/5 23:56
"""
from rest_framework.serializers import ModelSerializer

from api.models import TodoItem


class TodoItemSerializer(ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'
