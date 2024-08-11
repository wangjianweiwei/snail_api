from datetime import timedelta, datetime

from django.db.models import Q
from django.utils import timezone
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from api.models import TodoItem
from api.serializers import TodoItemSerializer


class TodoItemViewSet(ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ("status", 'created_at')

    def filter_queryset(self, queryset):
        status = self.request.query_params.get('status')
        date = self.request.query_params.get('date')
        query = Q()
        if status:
            query &= Q(is_completed=status)

        if date:
            date = timezone.datetime.strptime(date, '%Y-%m-%d').date()
            query &= Q(completed_at__date=date) if status and int(status) else Q(plan_at=date)

        return queryset.filter(query)
