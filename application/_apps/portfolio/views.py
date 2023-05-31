import json, os
from django.conf import settings
from django.shortcuts import render

def load_json():
    with open(os.path.join(settings.BASE_DIR, '_root', 'database', 'profile.json'), encoding='utf-8') as f:
        data = json.load(f)
    return {
        'full_name': data['first_name'] + ' ' + data['middle_initial'] + ' ' + data['last_name'],
        'first_name': data['first_name'] + "'s",
        'introduction': data['introduction'],
        'description': data['description'],
        'github_link': data['github_link'],
        'facebook_link': data['facebook_link'],
        'contact_me_description': data['contact_me_description'],
        'school': data['school'],
        'likes': data['likes'],
        'dislikes': data['dislikes'],
        'app_experties': data['app_experties'],
        'known_languages': data['known_languages'],
        'projects': data['projects'],
    }

def index(request):
    context = load_json()
    return render(request, 'portfolio/index.html', context)
