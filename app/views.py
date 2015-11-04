from flask import url_for, jsonify, render_template, request, redirect
from datetime import datetime

from app import app, db
from .models import Note


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('content'):
            note = Note(content=request.form['content'], timestamp=datetime.utcnow())
            db.session.add(note)
            db.session.commit()
            rendered = render_template('note.html', note=note)
            return jsonify({'note': rendered, 'success': True})
        return jsonify({'success': False})
    notes = Note.public().limit(50)
    # notes = []
    return render_template('index.html', note=notes)


@app.route('/archive/<int:pk>', methods=['GET', 'POST'])
def archive(pk):
    note = Note.query.filter_by(id=pk).first()
    if note is None:
        return redirect(url_for('index'))
    note.archived = True
    db.session.add(note)
    db.session.commit()
    return jsonify({'success': True})
