import datetime
from models import likes_in_day_table
import db_session
from models import Projects
from flask import abort
from PIL import Image, ImageDraw
import os
from sqlalchemy.orm import subqueryload
import matplotlib.pyplot as plt
import numpy


def plot_avg_likes(likes, dates):
    fig = plt.figure()
    plot = fig.add_subplot(111)
    x = dates
    y = likes
    plot.plot(x, y)
    fig.canvas.draw()
    w, h = fig.canvas.get_width_height()
    numpy_img_arr = numpy.frombuffer(fig.canvas.tostring_rgb(), dtype=numpy.uint8).reshape(h, w, 3)
    img = Image.fromarray(numpy_img_arr)
    print(img.size)
    img.save('from_numpy.png')


def get_popular_projects():
    sesion = db_session.create_session()
    projects = sesion.query(Projects). \
        options(subqueryload(Projects.owner)). \
        order_by(Projects.avg_rate.desc()). \
        limit(5). \
        all()
    return projects


def get_recommended_projects(num=5):
    sesion = db_session.create_session()
    return sesion.query(Projects). \
        options(subqueryload(Projects.owner)). \
        limit(num). \
        all()


def resize_image(img_url, w, h):
    try:
        image = Image.open(img_url)
        new_image = image.resize((w, h))
        new_image.save(img_url)
        return 'OK'
    except Exception as e:
        return e


def write_new_likes():
    current_date = datetime.date.today()
    sesion = db_session.create_session()
    conn = db_session.create_coon()
    for project in sesion.query(Projects).all():
        values = {'rates_' + str(i): getattr(project, 'rates_' + str(i)) for i in range(1, 6)}
        print('values', values)
        values.update({'project_id': project.id, 'date': current_date})
        ins = likes_in_day_table.insert().values(**values)
        conn.execute(ins)
    conn.close()


def get_project(id):
    sesion = db_session.create_session()
    object_project = sesion.query(Projects).get(id)
    if object_project:
        return object_project
    abort(404)


# def get_comments(project_id):
#     session = db_session.create_session()
#     comments


def resize_image(image_name, w, h):
    try:
        path = os.path.join(os.getcwd(), os.path.join('static/imgs/project_imgs',
                                                      image_name))
        image = Image.open(path)
        new_image = image.resize((w, h))
        new_image.save(path)
        return 'OK'
    except Exception as e:
        return e


