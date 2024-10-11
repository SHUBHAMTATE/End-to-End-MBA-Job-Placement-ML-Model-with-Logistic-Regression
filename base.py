from flask import Flask, render_template, request
import pandas as pd
import pickle #import pickle 
#Create
app = Flask(__name__)

def prediction_input_data(input_df):
    # Load the column transformer and logistic regression model
    ct = pickle.load(open("coltransformer.pkl", "rb"))
    lr = pickle.load(open("logmodel.pkl", "rb"))

    # Apply the column transformer to the input data
    x = ct.fit_transform(input_df)

    # Make predictions
    ans = lr.predict(x)[0]

    if ans == 1:
        return "You have a strong chance of securing the job.\n🤓"
    else:
        return "it's possible that you may not be selected for the job.😟"

@app.route("/")
def display_form():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def get_input_data():
    # Retrieve data from the form
    gender = request.form.get("GENDER")
    sscboard = request.form.get("sscboard")
    sscmarks = float(request.form.get("sscmarks"))
    hscboard = request.form.get("hscboard")
    hscmarks = float(request.form.get("hscmarks"))
    subject = request.form.get("subject")
    degreemarks = float(request.form.get("degreemarks"))
    drgreename = request.form.get("degree")
    experience = request.form.get("experience")  # Assuming experience is an integer
    empmarks = float(request.form.get("empmarks"))
    specialisation = request.form.get("specialisation")
    mba_percent = request.form.get("mba_percent")
    # Create a DataFrame with the input data {'emp_test_percentage', 'hsc_percentage', 'ssc_percentage', 'degree_percentage'}
    input_df = pd.DataFrame(data=[[gender, sscmarks, sscboard, hscmarks, hscboard, subject, degreemarks, drgreename, experience, empmarks, specialisation, mba_percent]],
                            columns=['gender', 'ssc_percentage', 'ssc_board', 'hsc_percentage', 'hsc_board',
                                    'hsc_subject', 'degree_percentage', 'undergrad_degree','work_experience', 'emp_test_percentage', 'specialisation','mba_percent'])

    # Make predictions and pass the result to the display template 
    ans = prediction_input_data(input_df)
    return render_template("display.html", data=ans)

if __name__ == "__main__":
    app.run(debug=True)
















# from flask import*
# import pandas as pd
# import numpy as np
# import pickle

# app=Flask(__name__) 
# def predictioninputdat(input_df):
#     ct=pickle.load(open("coltransformer.pkl","rb"))
#     lr=pickle.load(open("logmodel.pkl","rb"))
#     x=ct.fit_transform(input_df)
#     ans=lr.predict(x)[0]
#     if ans==1:
#         return "your will get job"
#     else:
#         return "your will not get job"
    

# @app.route("/")

# def displayform():
#     return render_template("home.html")

# @app.route("/reglink",method="post")

# def getinputdata():
#     gender=request.form["GENDER"]
#     sscboard=Request.form["sscboard"]
#     sscmarks=float(Request.form["sscmarks"])
#     hscboard=Request.form["hscboard"]
#     hscmarks=float(Request.form["hscmarks"])
#     hscboard=Request.form["hscmarks"]
#     subject=Request.form["subject"]
#     degreemarks=float(Request.form["degreemarks"])
#     drgreename=Request.form["degree"]
#     Exprience=Request.form["Exprience"]
#     empmarks=float(request.form["empmarks"])
#     specialisation=request.form["specialisation"]
#     input_df=pd.DataFrame(data=[[gender,sscmarks,sscboard,hscmarks,hscboard,subject,degreemarks,drgreename,Exprience,empmarks,specialisation,]],columns=[])

#     ans=predictioninputdat(input_df)
#     return render_template("display.html",data=ans)

# if(__name__=="__main__"):
#     app.run(debug=True)
