from functions.authentication   import admin_auth, validate_user
from functions.anime_get_lists  import ep_num, get_anime_list, get_anime, get_canvas
from django.shortcuts import redirect, render
from django.urls      import reverse

# Create your views here.

def homepage(request, *args, **kwargs):
    if validate_user(request):
        first, second, third = get_canvas()

        ginger = {
            'animes' : get_anime_list(),
            'first'  : first,
            'second' : second,
            'third'  : third,
        }
        return render(request, 'index.html', ginger)
    else:
        return redirect(reverse('login'))


def watch(request, *args, **kwargs):
    if validate_user(request):
        if 'anime' in kwargs:
            anime_name = kwargs['anime']
            ep = 1
        else:
            return redirect(reverse('homepage'))

        anime = get_anime(anime_name)
        anime_eps        = ep_num(anime['Episodes'])
        anime_current_ep = anime['Episodes'][int(ep)-1]

        ginger = {
            'name'           : anime_name,
            'eps'            : anime_eps,
            'current_ep_link': anime_current_ep,
            'current_ep'     : ep,
        }
        return render(request, 'watch.html', ginger)
    else:
        return redirect(reverse('login'))
