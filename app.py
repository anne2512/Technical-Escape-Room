from flask import Flask, render_template, url_for, request, redirect,session, flash
import openpyxl
import jumble

app = Flask(__name__)



app.secret_key = "whyareyouseeingthis"


oe, je , od , jd = [], [], [], []


@app.route("/",methods=["GET","POST"])
def home():
    

    global oe
    global je
    if not session.get('firste') :  
        oe ,je = jumble.get_easy()
        session["firste"] = True
        print('Easy loaded')

    easy1_original , easy1_jumble = oe,je
    if request.method == "POST" :


        easy1_user = request.form.getlist("codePiece")
        if easy1_user == easy1_original :
            session["easy_won"] = True
            return redirect("/diff")
        else:
            session["Wrong"] = True
    
            print("user {} \n jumbled {} \n original {}".format(easy1_user,easy1_jumble,easy1_original))


    return render_template("sympo.html",easy1_original=easy1_original,easy1_jumble=easy1_jumble)



@app.route("/diff",methods=["GET","POST"])
def home_difficult():
    if session.get('easy_won'):
        global od
        global jd
        if not session.get("firstd") :  
            od ,jd = jumble.get_difficult()
            session["firstd"] = True
            print('Difficult loaded')

        diff1_original , diff1_jumble = od,jd
        if request.method == "POST" :


            diff1_user = request.form.getlist("codePiece")
            if diff1_user == diff1_original :
                session["diff_won"] = True
                return redirect("/win")
            else:
                session["Wrong"] = True
        
                print("user {} \n jumbled {} \n original {}".format(diff1_user,diff1_jumble,diff1_original))


        return render_template("sympo_d.html",easy1_original=diff1_original,easy1_jumble=diff1_jumble)
    else:
        return redirect('/')

@app.route("/win")
def win():
    if session.get("easy_won") and session.get("diff_won"):
        return render_template("win.html")
    return redirect('/')

@app.route('/ref')
def ref():

    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

