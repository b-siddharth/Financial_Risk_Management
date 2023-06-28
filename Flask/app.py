from flask import Flask, render_template, request
app = Flask(__name__)

import pickle
model = pickle.load(open('risk.pkl', 'rb'))

@app.route("/")
def helloworld():
    return render_template('base.html')

@app.route("/assessment")
def prediction():
    return render_template('index.html')

@app.route('/risk', methods=['POST'])
def admin():
    
    q = request.form["gender"]
    if(q == "f"):
        q = 0
    if(q == "m"):
        q = 1
    
    r = request.form["housing"]
    if( r == "own"):
        r1, r2, r3 = 0,1,0
    if( r == "free"):
        r1, r2, r3 = 1,0,0
    if( r == "rent"):
        r1, r2, r3 = 0,0,1
        
    s = request.form["job"]
    if( r == "un"):
        s = 0
    if( r == "ur"):
        s = 1
    if( r == "sk"):
        s = 2
    if( r == "hs"):
        s = 3
        
    t = request.form["saving"]
    if( t == "l"):
        r1, t2, t3, t4 = 0,0,0,1
    if( t == "m"):
        r1, t2, t3, t4 = 0,1,0,0
    if( t == "qr"):
        t1, t2, t3, t4 = 0,0,1,0
    if( r == "r"):
        t1, t2, t3, t4 = 0,0,0,1
        
    u = request.form["checking"]
    if( u == "lt"):
        u1, u2, u3 = 1,0,0
    if( u == "mo"):
        u1, u2, u3 = 0,1,0
    if( u == "ri"):
        u1, u2, u3 = 0,0,1
        
        
    v = request.form["credit"]
    
    w = request.form["duration"]
    
    x = request.form["purpose"]
    if(x == 'bu'):
        x1, x2, x3, x4, x5, x6, x7, x8 = 1,0,0,0,0,0,0,0
    if(x == 'car'):
        x1, x2, x3, x4, x5, x6, x7, x8 = 0,1,0,0,0,0,0,0
    if(x == 'da'):
        x1, x2, x3, x4, x5, x6, x7, x8 = 0,0,1,0,0,0,0,0
    if(x == 'edu'):
        x1, x2, x3, x4, x5, x6, x7, x8 = 0,0,0,1,0,0,0,0
    if(x == 'fe'):
        x1, x2, x3, x4, x5, x6, x7, x8 = 0,0,0,0,1,0,0,0
    if(x == 'rtv'):
        x1, x2, x3, x4, x5, x6, x7, x8 = 0,0,0,0,0,1,0,0
    if(x == 'rep'):
        x1, x2, x3, x4, x5, x6, x7, x8 = 0,0,0,0,0,0,1,0
    if(x == 'vo'):
        x1, x2, x3, x4, x5, x6, x7, x8 = 0,0,0,0,0,0,0,1
        
    y = [[int(x1), int(x2), int(x3), int(x4), int(x5), int(x6), int(x7), int(x8), int(r1), int(r2), int(r3), int(t1), int(t2), int(t3), int(t4), int(u1), int(u2), int(u3), int(v), int(w), int(s), int(q)]]
    
    a = model.predict(y)
    
    if (a[0] == 0):
        b = "Bad"
        return render_template("bad.html", z = b)
    if (a[0] == 1):
        b = "Good"
        return render_template("good.html", z = b)
    
    
    
    if __name__ == "__main__":
        app.run(debug = True)