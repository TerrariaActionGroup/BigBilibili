from flask import render_template, session, redirect, url_for, current_app,flash,abort
from flask.ext.login import login_required, current_user
from .. import db
from ..models import User,Permission,Post,Role
from ..email import send_email
from . import main
from .forms import NameForm,PostForm,EditProfileForm,EditProfileAdminForm
from ..decorators import admin_required

@main.route('/',methods=['GET','POST'])
def index():
	#form = PostForm()
	#if current_user.can(Permission.WRITE_ARTICLES) and \
	#		form.validate_on_submit():
	#	post = Post(body=form.body.data,
	#				author=current_user._get_current_object())
	#	db.session.add(post)
	#	return redirect(url_for('.index'))
	#posts = Post.query.order_by(Post.timestamp.desc()).all()
	#return render_template('index.html',form=form,posts=posts)
	return render_template('index.html')
	
@main.route('/user/<username>')
def user(username):
	user = User.query.filter_by(username=username).first()
	if user is None:
		abort(404)
	posts = user.posts.order_by(Post.timestamp.desc()).all()
	return render_template('user.html',user=user,posts=posts)

@main.route('/edit-profile',methods=['GET','POST'])
@login_required
def edit_profile():
	form = EditProfileForm()
	if form.validate_on_submit():
		current_user.name = form.name.data
		current_user.location = form.location.data
		current_user.about_me = form.about_me.data
		db.session.add(current_user)
		flash('Your profile has been updated.')
		return redirect(url_for('.user',username=current_user.username))
	form.name.data = current_user.name
	form.location.data = current_user.location
	form.about_me.data = current_user.about_me
	return render_template('edit_profile.html',form=form)

@main.route('/edit_profile/<int:id>',methods=['GET','POST'])
@login_required
@admin_required
def edit_profile_admin(id):
	user =User.query.get_or_404(id)
	form = EditProfileAdminForm(user=user)
	if form.validate_on_submit():
		user.email = form.email.data
		user.username = form.username.data
		user.confirmed = form.confirmed.data
		user.role = Role.query.get(form.role.data)
		user.name = form.name.data
		user.location = form.location.data
		user.about_me = form.about_me.data
		db.session.add(user)
		flash('The profile has been updated.')
		return redirect(url_for('.user',username=user.username))
	form.email.data = user.email
	form.username.data = user.username
	form.confirmed.data = user.confirmed
	form.role.data = user.role_id
	form.name.data = user.name
	form.location.data = user.location
	form.about_me.data = user.about_me
	return render_template('edit_profile.html', form=form, user=user)

@main.route('/video/<avnumber>', methods=['GET', 'POST'])
def video(avnumber):
	fileName = 'video/' + avnumber + '.mp4'
	filesrc = url_for('static', filename = fileName)
	comments = ['1','2','3','4']

	return render_template('video.html',av=filesrc, comments=comments)

@main.route('/dance/', methods=['GET', 'POST'])
def dance():
	lists = ['1','2','3','4','5','2','3','4','5','2','3','4']
	rank1 = ['1', '2', '3']
	rank2 = ['4','5', '6' ,'7', '8', '9', '10']
	return render_template('dance.html',vlist=lists, rank1=rank1, rank2=rank2)

@main.route('/video_submit/', methods=['GET', 'POST'])
def video_submit():
	return render_template('video_submit.html')
