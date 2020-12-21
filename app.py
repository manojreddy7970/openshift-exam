from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
   key = os.getenv("KEY")
   file = os.getenv("FILE")
   print(key)
   return 'Hello World'

if __name__ == '__main__':
   app.run(host='0.0.0.0')
