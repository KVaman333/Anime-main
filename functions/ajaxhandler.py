from firebase_admin import db



def clean_url(url):
    url = url.replace('%20', ' ')
    return url


def ep_frame(anime, ep):
    database = db.reference(f'Series/All/{anime}/')
    database = database.get()

    frame = database['Episodes'][int(ep)-1]
    return frame