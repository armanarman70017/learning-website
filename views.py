from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Courses, MyCourses
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
  if request.method == 'POST':
    note = request.form.get('note')  #Gets the note from the HTML

    if len(note) < 1:
      flash('Note is too short!', category='error')
    else:
      new_note = Note(
          data=note,
          user_id=current_user.id)  #providing the schema for the note
      db.session.add(new_note)  #adding the note to the database
      db.session.commit()
      flash('Note added!', category='success')

    course = request.form.get('course')  #Gets the course from the HTML
    if len(course) < 1:
      flash('Course is too short!', category='error')
    else:
      new_course = MyCourses(
          courseId='3',
          userId=current_user.id)  # providing the schema for the note
      db.session.add(new_course)  # adding the note to the database
      db.session.commit()
      flash('Course added!', category='success')

  courses = Courses.query.filter_by(courseId='2').first()

  return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
  note = json.loads(
      request.data)  # this function expects a JSON from the INDEX.js file
  noteId = note['noteId']
  note = Note.query.get(noteId)
  if note:
    if note.user_id == current_user.id:
      db.session.delete(note)
      db.session.commit()

  return jsonify({})


@views.route('/delete-course', methods=['POST'])
def delete_course():
  course = json.loads(
      request.data)  # this function expects a JSON from the INDEX.js file
  courseid = course['courseId']
  course = MyCourses.query.get(courseid)
  if course:
    if course.userId == current_user.id:
      db.session.delete(course)
      db.session.commit()

  return jsonify({})


def select_courses():
  courseId = 2
  course = Courses.query.get(courseId)
