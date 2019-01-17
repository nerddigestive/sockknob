import time

from flask import url_for, request, render_template, jsonify
from app import app


app.is_sock_on_door = False
app.sock_set_time = time.time()


@app.route('/')
def index():
	if app.is_sock_on_door:
		return render_template('on.html')
	else:
		return render_template('off.html')


@app.route('/api/sock/on', methods=['POST'])
def sock_on():
	app.is_sock_on_door = True
	app.sock_set_time = time.time()
	return get_state()


@app.route('/api/sock/off', methods=['POST'])
def sock_off():
	app.is_sock_on_door = False
	app.sock_set_time = time.time()
	return get_state()


@app.route('/api/sock', methods=['GET'])
def get_state():
	return jsonify({'state': app.is_sock_on_door,
			 		'duration': time.time() - app.sock_set_time})


@app.route('/api/sock', methods=['POST'])
def set_sock():
	json_data = request.args.get_json()
	sock_state = json_data.get('onDoor', None)

	try:
		assert type(sock_state) is bool
	except AssertionError, e:
		print("HTTP-400: Attempt to set invalid sock state.")
		return jsonify({'error': 'Attempt to set invalid sock state.'}), status.HTTP_400_BAD_REQUEST
	
	app.is_sock_on_door = sock_state
	app.sock_set_time = time.time()

	if app.is_sock_on_door:
		print("Sock is now on the door handle...")
	else:
		print("Sock has now been removed from the door handle...")
	
	return get_state()

