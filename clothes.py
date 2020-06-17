from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from.models import Destination, Comment
from.forms import DestinationForm, CommentForm
from .import db

# Create a blueprint
bp= Blueprint('destination',_name_,url_prefix='/destinations')


@bp.route('/<id>')
def show(id):
#destination = get_destination()
destination = Destination.query.filter_by(id=id)first()
cform = CommentForm()
return render_template('destinations/show.html, destination=destination, form =cform)

@bp.route('/<id>/comment' methods=['GET', 'POST'])
def comment(id)
destination = Destination.query.filter_by(id=id).first()
cform = CommentForm()
if cform.validate_on_submit():
    comment = Comment(text=cform.text.data, destination=destination)


    db.session.add(comment)
    db.session.commit()
    print('Your comment has been added,'success')
return render_template('destinations/show.html, destination= destination, form=cform')





