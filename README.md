# rest_over_http

For run this project please follow the instructions

1. create virtual environment in python3
  ```
  virtualenv -p python3 <env name>
  ```
2. install requirements file for all dependencies

  ```
  pip install -r requiremets.txt
  ```
3.Run application 

  ```
  FLASK_APP=app.py flask run
  ```
  it give an output like 
  ```
  * Serving Flask app "app.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```
4. user REST reuest : for exampe use postman app and access the url and pass JSON data with POST method

  ```
  http://127.0.0.1:5000/sendata
  ```
  send data
  ```
  {
	"test":"test"
  }
  ```
