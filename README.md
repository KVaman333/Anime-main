# Anime: A Simple Streaming Dashboard

A small Django web app where signed-in users browse an anime catalogue and watch episodes in an embedded player. The catalogue, episode links and user accounts are stored in Firebase Realtime Database. The interface switches episodes without reloading the page.

> **Note:** This project does not host or store any video files. Episodes are embedded from third-party players, and the project was built for learning. Please respect the terms of service and copyright of the content owners.

## Features

- **Login-protected access:** visitors must sign in before they can reach the homepage or the player.
- **Homepage with featured banner:** a hero section with three featured titles plus the full anime list.
- **Watch page:** pick any show and play its episodes in an embedded player.
- **Instant episode switching:** an AJAX request loads the chosen episode into the player without refreshing the page.
- **Admin-aware accounts:** each user has a category (such as `admin`) stored alongside their credentials.
- **Cloud-backed content:** shows, episodes and users all live in Firebase Realtime Database, so content can be updated without redeploying.

## Tech Stack

| Area | Technology |
|---|---|
| Language | Python 3.9.7 |
| Framework | Django 3.2 |
| Database | Firebase Realtime Database via `firebase-admin` |
| Frontend | Django templates, Bootstrap, jQuery (AJAX), Plyr, Owl Carousel |
| Deployment | Gunicorn, WhiteNoise |

## Project Structure

```
.
├── Anime/           # Django project settings, URLs, WSGI/ASGI
├── login/           # Login and logout views and template
├── dashboard/       # Homepage and watch page views and templates
├── ajaxhandler/     # AJAX endpoint for switching episodes
├── functions/       # Firebase helpers: authentication, anime lists, episode lookup
├── templates/       # Shared base templates
├── static/          # CSS, JavaScript, fonts and images
├── manage.py
├── requirements.txt
└── runtime.txt
```

## How It Works

1. A user opens the site and is redirected to the login page.
2. The login view checks the submitted username and password against the `Users` node in Firebase and sets a cookie on success.
3. The homepage loads the featured banner items and the anime list from Firebase and renders them.
4. Opening a show loads its episode list and plays episode 1 in the embedded player.
5. Clicking another episode sends a request to `/ajaxhandler/switch-episode/`, which returns that episode's embed link, and the player updates in place.

### Routes

| Route | Purpose |
|---|---|
| `/` | Redirects to the login page |
| `/dashboard/homepage/` | Catalogue and featured banner |
| `/dashboard/watch/<anime>/` | Player for a given show |
| `/ajaxhandler/switch-episode/` | Returns the embed link for a requested episode |
| `/admin/` | Django admin |

## Firebase Data Structure

The app expects a Realtime Database shaped like this:

```
Users/
  <username>/
    password: ...
    Category: "admin" | ...
Series/
  Canvas/
    First-Item: ...
    Second-Item: ...
    Third-Item: ...
  All/
    <Anime Name>/
      Episodes: [ "<embed link for ep 1>", "<embed link for ep 2>", ... ]
```

Episode links are collected separately and added to the database, so the repo contains no video sources.

## Getting Started

### Prerequisites

- Python 3.9 (the project is pinned to 3.9.7)
- A Firebase project with Realtime Database enabled
- A Firebase service-account key (generated from your own Firebase project)

### Installation

```bash
git clone https://github.com/KVaman333/Anime-main.git
cd Anime-main

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac / Linux

pip install -r requirements.txt
```

### Configure Firebase and secrets

1. Save your service-account key as `Anime/api.json`. **Never commit this file.** Add it to `.gitignore`.
2. In `Anime/settings.py`, replace the placeholder `databaseURL` and `storageBucket` with your own project's values.
3. Replace the placeholder `SECRET_KEY` with a new random value. Better still, load it from an environment variable.
4. Add data to your database following the structure above.

### Run

```bash
python manage.py migrate
python manage.py runserver
```

Open **http://127.0.0.1:8000** and sign in with a user you created in Firebase.

## Known Limitations

- This is a learning project, and its authentication is intentionally simple. It is not suitable for production use as-is.
- `DEBUG` is on and `ALLOWED_HOSTS` is open by default, which should be changed before any deployment.
- Dependencies are pinned to 2021 versions.
- There are no automated tests.

## Author

**Kunal Vaman Dwivedi**
[GitHub](https://github.com/KVaman333) · [LinkedIn](https://linkedin.com/in/kunal-vaman-285200436)
