from flask import Flask, render_template,request,jsonify
from solve import solver, webSolver, solverRaw
from flask_cors import CORS




app = Flask(__name__)
CORS(app)

@app.route('/',methods = ['GET'])
@app.route('/send',methods = ['GET','POST'])
def send():
	if request.method == 'POST':
		middle = request.form['middle']
		outside = request.form['outside']
		result = solver(middle, outside)
		return render_template('result.html',result=result)
	return render_template('index.html')

@app.route('/api/create', methods=['GET'])
def api_create():
	if 'out' in request.args and 'middle' in request.args:
		middleLetter = str(request.args['middle'])
		outsideLetters = str(request.args['out'])
		# return("Middle letter: " + middleLetter + ". Outside Letters: " + outsideLetters)
		solved = solverRaw(middleLetter, outsideLetters)
		resp = jsonify({"words": solved})
		print(resp)
		return resp
	else:
		resp = jsonify("Error")
	return render_template('index.html')

@app.route('/api/status', methods=['GET'])
def status():
	return(jsonify(200))

@app.route('/sendWeb',methods = ['GET','POST'])
def sendWeb():
	if request.method == 'POST':
		result = webSolver()
		return render_template('webResult.html',result=result)
	return render_template('index.html')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, threaded=True)
