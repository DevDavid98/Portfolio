from flask import (render_template, redirect, url_for, request)
from app_db import db, Projects, app


# Home page
@app.route('/')
def index():

    projects = Projects.query.all()
    return render_template('index.html', projects=projects)


# Add project form
@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.form:

        new_project = Projects(
            title=request.form['title'],
            completed=request.form['date'],
            description=request.form['desc'],
            skills=request.form['skills'],
            link=request.form['github'])

        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))

    projects = Projects.query.all()

    return render_template('new_project_form.html', projects=projects)


@app.route('/project/<id>')
def project(id):

    projects = Projects.query.all()
    project = Projects.query.get_or_404(id)
    project_skills = []

    for skill in project.skills.split(","):
        project_skills.append(skill)

    return render_template(
        'detail.html',
        project=project,
        project_skills=project_skills,
        projects=projects)


# Edit project form
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):

    project = Projects.query.get(id)

    if request.form:

        project.title = request.form['title']
        project.completed = request.form['date']
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.link = request.form['github']
        db.session.commit()

        return redirect(url_for('index'))

    projects = Projects.query.all()

    return render_template(
        'edit_project_form.html',
        project=project,
        projects=projects)


# Delete Project
@app.route('/delete/<id>')
def delete(id):

    project = Projects.query.get(id)
    db.session.delete(project)
    db.session.commit()

    return redirect(url_for('index'))


# About me page
@app.route('/about')
def about():

    projects = Projects.query.all()
    return render_template('about.html', projects=projects)


if __name__ == '__main__':

    db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')
