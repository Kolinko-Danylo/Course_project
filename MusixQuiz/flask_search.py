from flask import Flask, render_template, redirect, url_for, request, make_response, session
from musixmatch_request import get_track_id, get_track_lyrics
from forms import SearchForm, WordsForm
import quizlet_user_auth as q
from urllib.request import urlopen

app = Flask(__name__)

app.config['SECRET_KEY'] = '2a54879bd37d3d1a2e68479fda4c23c9'

my_app = q.Quizlet(client_id='vDYMbQXMZR',
                           encoded_auth_str='dkRZTWJRWE1aUjpxbTJ5ajZKanIzdVRnOHc3TWhjRVVH',
                           redirect_uri="http://kolinkodanylo.pythonanywhere.com/")

@app.route('/', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        tup = my_app.generate_auth_url('write_set')
        return redirect(tup[0])
    code = request.args.get("code")
    if code == None:
        return render_template('home.html')
    session['user'] = code
    return redirect("http://kolinkodanylo.pythonanywhere.com/search")



@app.route('/about')
def about():
    return render_template('about.html', title='Daniel blog')


@app.route('/lyrics')
def lyrics(author, song, lyrics):
    return render_template('song_lyrics.html', author=author, name=song, lyrics=lyrics)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if 'user' not in session:
        return redirect("http://kolinkodanylo.pythonanywhere.com/")
    form = SearchForm()
    words_form = WordsForm()

    if form.validate_on_submit():
        author_name = form.author_name.data
        song_name = form.song_name.data
        track_id = get_track_id(author_name, song_name)
        if track_id == 'nothing_found' or track_id == 'no_lyrics':
            pass
        else:
            song_lyrics = get_track_lyrics(track_id)
            return render_template('song_lyrics.html', author=author_name, name=song_name, lyrics=song_lyrics, form=words_form)
    return render_template('search.html', title='Search', form=form)


@app.route('/saveWords', methods=['POST'])
def save_words():
    form = WordsForm()
    if form.validate_on_submit():
        words = form.words.data.split()

        print("Words")
        print(words)
        print(len(words))

        my_app.request_token(session['user'])
        my_app.add_set('title', words, [' ' for i in range(len(words))], 'en', 'en')

    return "Successfully saved words: " + ", ".join(words) + "!"
