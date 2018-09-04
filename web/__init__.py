import string 
import couchdb 
from flask import * 
import Database 
import Vehicle
from Database import *
from Vehicle import *

app = Flask(__name__)
app.config.update(
    DATABASE = 'Arlton'
)
#db = couchdb.Server("http://localhost:5984/")[app.config["DATABASE"]]
global db
global login 
global vinfo

db = Database("http://localhost:5984")
login = False
vinfo = None


@app.errorhandler(404)
def page_not_found(e):
    return render_template("/404.html")

@app.route("/", methods=["GET", "POST"])
def index():
    global db
    global login 
    global vinfo
    if(login):
        return dashboard()
    if request.method == "POST":
        try:
            uid = request.form['login']
            upass = request.form['password']
            if db.validateUser(uid, upass):
                login = True
                return render_template("/dashboard.html")
            else:
                return "Incorrect Username/Password"
        except Exception as ex:
            print(ex)
            return render_template("/500.html")
    return render_template("/index.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    global db
    global login 
    global vinfo
    if login:
        if request.method == "POST":
            try:
                vnum = request.form['number']
                a = db.getVehicle(vnum)
                if a:
                    vinfo = Vehicle(a)
                    
            except Exception as ex:
                print(ex)
                return render_template("/500.html")   
            return render_template("/dashboard.html", milage = vinfo.values['milage'], fuel = vinfo.values['fuel'], total_distance = vinfo.values['total_distance'], vnum = vinfo.values['vnum'], total_tires = vinfo.values['total_tires'], tires = json.dumps(vinfo.tires))
        return render_template("/dashboard.html")
    else:
        return render_template("/index.html") #Fool them, they would think it dosen't exist until they log in

if __name__ == '__main__':
   app.run()