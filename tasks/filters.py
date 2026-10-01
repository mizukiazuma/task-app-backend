from django.db.models import Q
from django_filters import rest_framework as filters

from .models import Task


class TaskFilter(filters.FilterSet):
    status =filters.CharFilter(field_name="status")
    q = filters.CharFilter(method="search_q", label="q")

    class Meta:
        model = Task
        fields = ("status","q",)
    def search_q(self, queryset, name, value):
        return queryset.filter(
            Q(title__contains=value) | Q(description__contains=value)
        )