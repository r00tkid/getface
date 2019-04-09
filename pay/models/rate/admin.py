from django.contrib.admin import ModelAdmin as _Admin
from django.utils.html import format_html as _format


class RateAdmin(Base.Admin):
    list_display = ('name', 'per_month', 'is_archived', 'id')
