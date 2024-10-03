from django import template

register = template.Library()


@register.filter(name='get_name')
def anime_name(anime,json):
    return json[anime]['Name']

@register.filter(name='get_cover')
def anime_cover(anime,json):
    return json[anime]['Cover']

@register.filter(name='get_link')
def anime_link(anime,json):
    return json[anime]['Link']

@register.filter(name='get_total_ep')
def anime_total_ep(anime,json):
    return json[anime]['Total Episodes']

@register.filter(name='get_present_ep')
def anime_present_ep(anime,json):
    return json[anime]['Present Episodes']

@register.filter(name='get_lang')
def anime_lang(anime,json):
    return json[anime]['Lang']

@register.filter(name='ep_link')
def ep_link(anime,ep_num):
    return anime['Episodes'][int(ep_num)-1]

##  CANVAS FILTERS  ##

@register.filter(name='canvas_pic')
def canvas_pic(anime):
    return anime['Landscape']

@register.filter(name='canvas_link')
def canvas_link(anime):
    return anime['Link']

@register.filter(name='canvas_name')
def canvas_name(anime):
    return anime['Name']

@register.filter(name='canvas_description')
def canvas_description(anime):
    return anime['Description']

@register.filter(name='canvas_tags')
def canvas_tags(anime):
    return anime['Tags']




