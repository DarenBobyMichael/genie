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
    prompt_answer = "\n"+query(request.args.get('user_input', 'mutton curry preperation'))
    print(prompt_answer)
#     prompt_answer = request.args.get('user_input',None)
#     prompt_answer = '''
#     Hello mofos
#     Ingredients:
#     1. 2 cups sushi rice
#     2. 1/3 cup rice vinegar
#     3. 10 sheets of nori (dried seaweed)
#     4. 1/2 lb sushi-grade raw fish (tuna, salmon etc)
#     5. 1 cucumber
#     6. 1 avocado
#     7. Soy sauce, Wasabi and pickled ginger for serving
# '''
    return render_template("display.html",prompt_answer = prompt_answer)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
