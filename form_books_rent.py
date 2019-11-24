from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, SubmitField, BooleanField, TextField
from wtforms.validators import DataRequired, NumberRange, Email, EqualTo


class RentCalcForm(FlaskForm):
    regular_books_count = IntegerField('regular_books_count',
                           validators=[NumberRange(min=0)])
    regular_rent_duration = IntegerField('regular_rent_duration',
                           validators=[NumberRange(min=0)])
    fiction_books_count = IntegerField('fiction_books_count',
                           validators=[NumberRange(min=0)])
    fiction_rent_duration = IntegerField('fiction_rent_duration',
                           validators=[NumberRange(min=0)])
    novel_books_count = IntegerField('novel_books_count',
                           validators=[NumberRange(min=0)])
    novel_rent_duration = IntegerField('novel_rent_duration',
                           validators=[NumberRange(min=0)])
    total = TextField("total", validators=[])
    submit = SubmitField('Submit')
