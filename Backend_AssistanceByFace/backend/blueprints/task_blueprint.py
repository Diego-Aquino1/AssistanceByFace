from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.task_model import TaskModel

task_blueprint = Blueprint('task_blueprint', __name__)

model = TaskModel()

@task_blueprint.route('/task/add_student', methods=['POST'])
@cross_origin()
def create_task():
    content = model.add_student(request.json['Apellidos'], request.json['Nombres'], request.json['Correo'], request.json['Ciudad'], request.json['Foto'])
    return jsonify(content)

@task_blueprint.route('/task/delete_student', methods=['POST'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_student(int(request.json['CUI'])))

@task_blueprint.route('/task/get_student', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_student(int(request.json['CUI'])))

@task_blueprint.route('/task/get_students', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_students())


#######################################


@task_blueprint.route('/task/add_teacher', methods=['POST'])
@cross_origin()
def create_task_2():
    content = model.add_teacher(request.json['Apellidos'], request.json['Nombres'], request.json['Correo'], request.json['Ciudad'])
    return jsonify(content)

@task_blueprint.route('/task/delete_teacher', methods=['POST'])
@cross_origin()
def delete_task_2():
    return jsonify(model.delete_teacher(int(request.json['CUI'])))

@task_blueprint.route('/task/get_teacher', methods=['POST'])
@cross_origin()
def task_2():
    return jsonify(model.get_teacher(int(request.json['CUI'])))

@task_blueprint.route('/task/get_teachers', methods=['POST'])
@cross_origin()
def tasks_2():
    return jsonify(model.get_teachers())


######################################


@task_blueprint.route('/task/add_assitance', methods=['POST'])
@cross_origin()
def create_task_3():
    content = model.add_assistance(request.json['ASISTENCIA'], request.json['Fecha'], request.json['Asistencias'], request.json['Faltas'])
    return jsonify(content)

@task_blueprint.route('/task/get_assistance', methods=['POST'])
@cross_origin()
def taskID_3():
    return jsonify(model.get_assistance_ID(int(request.json['ID'])))

@task_blueprint.route('/task/get_assistance_ID', methods=['POST'])
@cross_origin()
def taskD_3():
    return jsonify(model.get_assistance_date((request.json['Fecha'])))

@task_blueprint.route('/task/get_assitances', methods=['POST'])
@cross_origin()
def tasks_3():
    return jsonify(model.get_assistances())

@task_blueprint.route('/task/delete_assistance', methods=['POST'])
@cross_origin()
def delete_task_3():
    return jsonify(model.delete_assistance((request.json['Fecha'])))


#######################################


@task_blueprint.route('/task/add_course', methods=['POST'])
@cross_origin()
def create_task_4():
    content = model.add_course(request.json['Nombre'])
    return jsonify(content)

@task_blueprint.route('/task/get_courses', methods=['POST'])
@cross_origin()
def tasks_4():
    return jsonify(model.get_courses())

@task_blueprint.route('/task/delete_course', methods=['POST'])
@cross_origin()
def delete_task_4():
    return jsonify(model.delete_course((request.json['Nombre'])))


#############################################


@task_blueprint.route('/task/add_group', methods=['POST'])
@cross_origin()
def create_task_5():
    content = model.add_group(request.json['Grupo'])
    return jsonify(content)

@task_blueprint.route('/task/get_groups', methods=['POST'])
@cross_origin()
def tasks_5():
    return jsonify(model.get_groups())

@task_blueprint.route('/task/delete_group', methods=['POST'])
@cross_origin()
def delete_task_5():
    return jsonify(model.delete_group((request.json['Grupo'])))