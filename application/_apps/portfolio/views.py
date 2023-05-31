import json, os
from django.conf import settings
from django.shortcuts import render

def load_json():
    with open(os.path.join(settings.BASE_DIR, '_root', 'database', 'profile.json')) as f:
        data = json.load(f)
    return {
        'full_name': data['first'] + ' ' + data['middle_initial'] + ' ' + data['last'],
        'first_name': data['first'] + "'s",
        'introduction': data['introduction'],
        'description': data['description'],
        'github_link': data['github_link'],
        'facebook_link': data['facebook_link'],
        'school': data['school'],
        'likes': data['likes'],
        'dislikes': data['dislikes'],
        'contact_me_description': data['contact_me_description'],
    }

def index(request):
    context = load_json()
    return render(request, 'portfolio/index.html', context)
