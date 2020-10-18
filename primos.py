import os
from Flask import Flask, jsonify, request
from math import sqrt

app = Flask (__name__)
@app.route('/')

def primos():
    ate = 100
    i = 2
    primo = '1,'
    while i <= ate:
        p = i % 2
        if p == 1:
            primo= primo + str(i)+','
        i = i + 1
    return primo


if __name__=='__main__':
    port - int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


