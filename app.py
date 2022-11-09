from flask import Flask,request, render_template ,redirect,flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey
from flask import session,make_response


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



@app.route("/question/<int:id>")
def qts(id):
    page=len(responses)
    
    if len(responses)!=id:
      flash('error','You dont have to skip the question')
      return redirect(f'/question/{page}')
    elif survey.questions ==0:
      return redirect('/')
    elif len(survey.questions) == page:  
      return redirect('/done')
   
    questions=survey.questions
    
    
    question=questions[page] 
    
    return render_template('question.html',question=question,questions=questions)



@app.route('/answer',methods=["POST"])
def answer():
    answer=request.form["answer"]
    session['RES']=responses
    responses.append(answer)
    print('***********')
    print(session['RES'])
    print('***********')
   
  
    
    return redirect(f'/question/{len(responses)}')
  
@app.route('/done')
def done():
    return render_template('done.html')
  
  
  



