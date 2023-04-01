from todoapp import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f'<User: {self.username} >'\
        

class Tododb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text)
    status = db.Column(db.Boolean, default=False)
    
    def __init__(self, create_by, title, desc, status = False):
        self.create_by = create_by
        self.title = title
        self.desc = desc
        self.status = status
    
    def __repr__(self):
        return f'<Tododb: {self.title} >'        