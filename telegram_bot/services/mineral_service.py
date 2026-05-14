from asgiref.sync import sync_to_async
from django_setup import *
from catalog.models import Mineral


@sync_to_async
def get_mineral_info(slug: str):
    try:
        mineral = Mineral.objects.get(slug=slug)
        return {
            "title": mineral.title,
            "formula": mineral.formula,
            "color": mineral.color,
            "hardness": mineral.hardness,
            "origin": mineral.origin,
            "usage": mineral.usage,
            "description": mineral.description,
            "facts": mineral.facts,
            "category": mineral.get_category_display() if mineral.category else "",
        }
    except Mineral.DoesNotExist:
        return None