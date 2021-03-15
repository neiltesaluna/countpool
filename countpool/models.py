from countpool import db

class Timer (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    goal = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Timer('{self.title}','{self.goal}')"
