from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user #as jwt_current_user

from .index import index_views

from App.controllers import (get_all_workouts, create_workout, add_exer_to_workout, get_workout_exercises, get_exercise, get_workout)

workout_views = Blueprint('workout_views', __name__, template_folder='../templates')

@workout_views.route('/workouts', methods =['GET'])
@workout_views.route('/workouts/<id>', methods =['GET'])
@jwt_required()
def get_workout_page(id=-1):
    workouts = get_all_workouts()
    workout_exercises = get_workout_exercises()

    sel_exercise = None

    if id == -1:
        pass
    else:
        sel_exercise = get_exercise(id)
    return render_template('workouts.html', workouts = workouts, workout_exercises=workout_exercises, sel_exercise=sel_exercise, current_user=current_user)

@workout_views.route('/workout_info', methods =['GET'])
@workout_views.route('/workout_info/<id>', methods =['GET'])
@jwt_required()
def get_workout_info_page(id=-1):
    workouts = get_all_workouts()
    workout_exercises = get_workout_exercises()

    sel_workout = None

    if id == -1:
        pass
    else:
        sel_workout = get_workout(id)
    return render_template('workout.html', workouts = workouts, workout_exercises=workout_exercises, sel_workout=sel_workout, current_user=current_user)

@workout_views.route('/workouts', methods=['POST'])
@jwt_required()
def create_workout_action():
    create_workout(request.form.get('exer_id'), "The workout is working", 81, current_user.id)#this is just a temp to test that workout model is working
    # add_exer_to_workout(1, 74, 4, 15)#use forms to get data and make it dynamic
    # add_exer_to_workout(1, 81, 500, 75)
    return redirect (url_for('workout_views.get_workout_page'))
    #return redirect (request.referrer)


@workout_views.route('/add_workout_exercise', methods=['POST'])
def add_workout_exercise():
    exercise_id = request.form.get('exercise_id')
    workout_id = request.form.get('workout_id')
    
    
    # add_exer_to_workout(1, 74, 4, 15)#use forms to get data and make it dynamic
    #add_exer_to_workout(1, 81, 500, 75)
    add_exer_to_workout(workout_id, exercise_id, 50, 37)
    return redirect(request.referrer)