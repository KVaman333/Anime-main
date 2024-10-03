from firebase_admin import db




def get_anime_list():
    database = db.reference('Series/All')
    database = database.get()

    return database


def get_anime(anime):
    database = db.reference('Series/All')
    database = database.get()

    return database[anime]





def ep_num(ep_list):
	count = []
	for i in range(len(ep_list)):
		count.append(i+1)
	return count


def get_canvas():
    database = db.reference('Series/Canvas/')
    database = database.get()

    first  = database['First-Item']
    second = database['Second-Item']
    third  = database['Third-Item']

    return first, second, third






