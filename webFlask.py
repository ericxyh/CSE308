from flask import Flask,render_template, request, jsonify
import search

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
	return render_template('main.html')

# finish search
@app.route("/search", methods=["POST"])
def searchReq():
	req = request.get_json();
	r = req['r']
	p = int(req['p'])
	#print(r,p,h2)
	ans = search.search(r,p)
	return jsonify(a = ans),200

if __name__ == "__main__":
#	app.debug = True
	app.run(host='0.0.0.0',port=80)