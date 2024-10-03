from functions.authentication import validate_user
from functions.ajaxhandler    import clean_url, ep_frame
from django.http.response     import JsonResponse
from django.shortcuts         import redirect, render
from django.urls      import reverse



def switch_ep(request, *args, **kwargs):
    if validate_user(request):
        if request.is_ajax():
            episode     = request.GET.get('requested_episode', False)
            current_show = clean_url(request.GET.get('current_url', False).split('/')[-2])
            frame = ep_frame(current_show, episode)
            response = {
                'frame'  : frame,
                'episode': episode
            }
            return JsonResponse(response,status=200)

        return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))
