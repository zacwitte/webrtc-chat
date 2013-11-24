from flask import Flask, request
app = Flask(__name__, static_url_path='', static_folder='')

@app.route('/')
def root():
	# return 'foo'
	return app.send_static_file('index.html')

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=9000, debug=True)