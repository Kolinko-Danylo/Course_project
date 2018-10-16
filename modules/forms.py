from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    """Search lyrics form."""
    author_name = StringField('Musician', validators=[DataRequired()])
    song_name = StringField('Song', validators=[DataRequired()])
    submit = SubmitField('Search!')


class WordsForm(FlaskForm):
    """Forming terms set form"""
    words = StringField('Words', validators=[DataRequired()])
    submit = SubmitField('Submit')
