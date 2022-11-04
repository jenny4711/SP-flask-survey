from flask import Flask,request, render_template 
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey


app=Flask(__name__) 

app.config['SECRET_KEY'] = "Don't tell anyone!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


responses=[]



@app.route('/')
def home_page():
  title=survey.title
  instructions=survey.instructions
  return render_template("home.html",title=title,instruction=instructions)



@app.route('/question')
def question():
  questions=survey.questions
  return render_template("question.html")



@app.route('/answer',methods=["POST"])
def answer():
    answer=request.form["answer"]
    responses.append(answer)
  
    return redirect('/question')
  
  
@app.route("/question/<int:id>")
def qts(id):
    page=len(responses)
    
    # if len(responses)!=id:
    #   return redirect(f'/question/{page}')
    # elif len(responses)==0:
    #   return redirect('/')
    # else:
    #   return redirect('/done')
    questions=survey.questions
    print(survey.questions[0])
    question=questions[len(responses)] 
    return render_template('question.html',question=question,questions=questions)


