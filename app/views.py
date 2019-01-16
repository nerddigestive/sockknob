from flask import url_for, redirect, request, render_template, flash, g, session, status
from app import app, lm


is_sock_on_door = False
sock_set_time = time.time()


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/api/sock/on', method=['POST'])
def sock_on():
	is_sock_on_door = True
	sock_set_time = time.time()
	return get_state()


@app.route('/api/sock/off', method['POST'])
def sock_off():
	is_sock_on_door = False
	sock_set_time = time.time()
	return get_state()


@app.route('/api/sock', methods=['GET'])
def get_state():
	return {'state': is_sock_on_door,
			'duration': time.time() - sock_set_time}


@app.route('/api/sock', methods=['POST'])
def set_sock():
	json_data = request.args.get_json()
	sock_state = json_data.get('onDoor', None)

	try:
		assert type(sock_state) is bool
	except AssertionError, e:
		print("HTTP-400: Attempt to set invalid sock state.")
		return {'error': 'Attempt to set invalid sock state.'}, status.HTTP_400_BAD_REQUEST
	
	is_sock_on_door = sock_state
	sock_set_time = time.time()

	if is_sock_on_door:
		print("Sock is now on the door handle...")
	else:
		print("Sock has now been removed from the door handle...")
	
	return get_state()

