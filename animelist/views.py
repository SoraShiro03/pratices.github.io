from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from .models import AnimeList

from taggit.models import Tag



def list_view(request, tag_slug=None):
   anime_list = AnimeList.objects.all()
   tag = None

   if tag_slug:
      tag = get_object_or_404(Tag, slug= tag_slug)
      anime_list = anime_list.filter(tags__in=[tag])


   paginator = Paginator(anime_list, 5)
   page = request.GET.get('page')

   try:
      anime_posts = paginator.page(page)
   except PageNotAnInteger:
      anime_posts = paginator.get_page(1)
   except EmptyPage:
      anime_posts = paginator.get_page(paginator.num_pages)

   
   context = {'anime_posts':anime_posts, 'page':page, 'tag':tag}
   return render(request, 'list_display/list.html', context)


def list_detail(request, year, month, day, anime_list):
   anime = get_object_or_404(AnimeList, slug=anime_list,
   date_posted__year = year,
   date_posted__month = month,
   date_posted__day = day
   )

   # list of similar anime.
   anime_tags_ids = anime.tags.values_list('id', flat=True)
   similar_anime_type = AnimeList.objects.filter(tags__in=anime_tags_ids)\
      .exclude(id=anime.id)

   similar_anime_type = similar_anime_type.annotate(same_tags=Count('tags'))\
      .order_by('-date_posted')[:5]



   context = {
      'anime':anime,
      'similar_anime_type':similar_anime_type,

      }
   return render(request, 'list_display/list_detail.html', context)
