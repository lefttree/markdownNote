import os
# -*- coding: utf-8 -*-

basedir = os.path.abspath(os.path.dirname(__file__))

# required by `FLASK-SQLAlchemy`
if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' + os.path.join(basedir, 'app.db') + '?check_same_thread=False')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
# where we store the SQLALchemy-migrate data files
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


