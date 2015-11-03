from flask import Markup
from markdown import markdown
from micawber import parse_html
from app import db, oembed


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime)
    archived = db.Column(db.Boolean, default=False)

    class Meta:
        database = db

    def html(self):
        """
        Run the content throught markdown, converts links into objects
        and return the html code
        """
        html = parse_html(
                markdown(self.content),
                oembed,
                maxwidth=300,
                urlize_all=True)
        return Markup(html)

    @classmethod
    def public(cls):
        return (Note
                .select()
                .where(Note.archived == False)
                .order_by(Note.timestamp.desc())
                )
