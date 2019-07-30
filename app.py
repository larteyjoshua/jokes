from flask import *
import requests,json
import os

app = Flask(__name__)
jokers=[]
@app.route('/')
def index():
    return render_template("jokes.html", jokers=jokers)

@app.route('/jokes', methods=["POST"])
def jokes():
    if request.method == "POST":
        firstname= request.form.get("firstname")
        lastname = request.form.get("lastname")
        print(firstname)
        print(lastname)
        r=requests.get('http://api.icndb.com/jokes/random?firstName='+firstname + '&lastName='+lastname)
        print(r.text)
        data=json.loads(r.text)
        yourjoke= data.get('value').get('joke')
        print(yourjoke)
        jokers.append(yourjoke)
        return redirect("/", code=302)


if __name__ == '__main__':
    port=os.environ.get('PORT', 5000)
    app.run(debug=True, host='0.0.0.0', port=port)
