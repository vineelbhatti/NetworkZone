import speedtest
from flask import *
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask("NetworkZone")
app.config['MONGO_URI'] = "mongodb+srv://vineelbhatti:27May1975@cluster0.ovfn9.mongodb.net/Vinellop?retryWrites=true&w=majority"

Bootstrap(app)

mongo = PyMongo(app)

app.config['SECRET_KEY'] = 'sOmE_rAnDom_woRd'

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        latest_speed = mongo.db.Me.find().sort('_id',-1).limit(1)
        new_speed = mongo.db.Me.find().sort('Speed', -1).limit(1)
        return render_template('home.html', vinell=new_speed, latest=latest_speed)

    elif request.method == 'POST':
        st = speedtest.Speedtest()
        flash('Please wait. Speed Test Running.')
        download = st.download()
        download = round(download*0.000000125, 1)
        emp_rec1 = {
            "Speed": download
        }
        for item in request.form:
            emp_rec1[item] = request.form[item]
        mongo.db.Me.insert_one(emp_rec1)
        return redirect('/')

if __name__== "__main__":
    app.run(host="https://git.heroku.com/networkzone.git", debug=True)

# app.run(debug=True)
