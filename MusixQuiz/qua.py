import quizlet_user_auth as q
from urllib import request

my_app = q.Quizlet(client_id='vDYMbQXMZR',
                   encoded_auth_str='dkRZTWJRWE1aUjpxbTJ5ajZKanIzdVRnOHc3TWhjRVVH',
                   redirect_uri='http://kolinkodanylo.pythonanywhere.com/')
my_app.request_token('DEKgR5HhGKSNrZZmhAsVUxNWFCaqE34chYTkXnF9')
my_app.add_set('title', ['terms', 'wef'], [' ',' '], [' ', ' '], ['',''])

