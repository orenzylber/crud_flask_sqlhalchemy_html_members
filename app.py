# HERE I WILL BUILD A FULL STACK WITH FRONT, BACK, DB & CLOUD
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# TODO: add CORS   -->    'TODO' is a programers way of writing notes & reminders

# create flask appliaction
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Members.db'
db = SQLAlchemy(app)

@app.route('/test')
def hello():
    return 'Hello, World!'

class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    membername = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return '<Members %r>' % self.membername

@app.route('/', methods=['GET', 'POST'])
def members():
    if request.method == 'GET':
        res=[]
        for memb in Members.query.all():
            res.append({"membername":memb.membername, "email":memb.email,"age":memb.age, "id":memb.id})
            # "membername" is connected to ${memb.membername} in line 40 in index.html
        return jsonify(res)
    elif request.method == 'POST': #add row
        member_data = request.get_json()
        member = Members(membername=member_data['membername'], email=member_data['email'], age=member_data['age'])
        db.session.add(member)
        db.session.commit()
        return jsonify({'id': member.id})

@app.route('/<int:member_id>', methods=['GET', 'PUT', 'DELETE'])
def member(member_id):
    member = Members.query.get(member_id)
    if not member:
        return jsonify({'error': 'Member not found'}), 404

    if request.method == 'GET':
        return   {"membername":member.membername, "email":member.email,"age":member.age ,"id":member_id}
    elif request.method == 'PUT':
        member_data = request.get_json()
        member.membername = member_data['membername']
        member.email = member_data['email']
        member.age = member_data['age']
        db.session.commit()
        return jsonify({'id': member.id})
    elif request.method == 'DELETE':
        db.session.delete(member)
        db.session.commit()
        return jsonify({'result': 'Member deleted'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
