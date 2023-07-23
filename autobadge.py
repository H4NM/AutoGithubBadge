import requests, sys

#Variables for the badges
python_version = sys.version.split(" ")[0]
app_version="1.1.5"
mood = "Happy :)"

#Badge data
badges = { "python_version": {"title": "Python",
                              "text": python_version,
                              "color": "blue",
                              "path": './py_badge.svg'},
           "app_version": {   "title": "App version",
                              "text": app_version,
                              "color": "green",
                              "path": './app_badge.svg'},
           "mood": {          "title": "Mood",
                              "text": mood,
                              "color": "yellow",
                              "path": './mood_badge.svg'},
           
           }

#Function for retrieving badges
def get_badge(text, variable, color):
    url="https://img.shields.io/badge/{}-{}-{}".format(text,variable,color)
    response = requests.get(url)
    if not response.status_code == 200:
        raise "Unable to reach url: {}".format(url)
    return response.text

#Iterating each badge in specified dict
for badge in badges:
    badge_data = get_badge(badges[badge]['title'],
                           badges[badge]['text'],
                           badges[badge]['color']) 
    with open(badges[badge]['path'], 'w') as file:
        file.write(badge_data)
        file.close()
