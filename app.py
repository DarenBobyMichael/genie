from flask import Flask, render_template, request, redirect, url_for
from query import query

app = Flask(__name__)

@app.route("/",methods =['GET','POST'])
def home():
    if request.method == 'POST':
        user_input = request.form.get('input_prompt')
        print(f"{user_input}")
        return redirect(url_for('display',user_input = user_input))
    return render_template("index.html", user_input = None)

@app.route("/display",methods =['GET','POST'])
def display():
    prompt_answer = query(request.args.get('user_input', 'mutton curry preperation'))
    return render_template("display.html",prompt_answer = prompt_answer)


if __name__ == "__main__":
    app.run(debug=True)
