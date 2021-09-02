from django import template
from ..models import AnimeList

register = template.Library()

@register.inclusion_tag('list_display/latest_anime.html')
def recently_added(count=6):
   latest_anime = AnimeList.objects.order_by('-date_posted')[:count]
   return {'latest_anime':latest_anime}