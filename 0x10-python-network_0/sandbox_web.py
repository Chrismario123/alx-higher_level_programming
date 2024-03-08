# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
# [GCC 9.4.0]
# Embedded file name: /tmp/web.py
# Compiled at: 2022-01-10 10:06:57
# Size of source mod 2**32: 2287 bytes
""" Doc
"""
from flask import Flask, Response, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'


@app.route('/route_1')
def route_1():
    return redirect(url_for('route_2'))


@app.route('/route_2')
def route_2():
    return 'Route 2'


@app.route('/route_3', methods=["'GET'", "'PUT'", "'OPTIONS'", "'DELETE'", "'POST'"])
def route_3():
    if request.method == 'DELETE':
        return "I'm a DELETE request"
    return "I'm not a DELETE request"


@app.route('/route_4', methods=['OPTIONS', 'HEAD', 'PUT'])
def route_4():
    res = Response('Did you GET it?')
    res.headers['Allow'] = 'OPTIONS, HEAD, PUT'
    return res


@app.route('/route_5')
def route_5():
    if request.headers.get('X-School-User-Id', '0') == '98':
        return 'Hello School!'
    return 'Who are you?'


@app.route('/route_6', methods=['POST'])
def route_6():
    get_keys = sorted(list(request.args.keys()))
    post_keys = sorted(list(request.form.keys()))
    result = []
    if len(get_keys) > 0:
        result.append('GET params:')
        for k in get_keys:
            result.append('\t{}: {}'.format(k, request.args.get(k)))

    if len(post_keys) > 0:
        result.append('POST params:')
        for k in post_keys:
            result.append('\t{}: {}'.format(k, request.form.get(k)))

    return '\n'.join(result)


@app.route('/route_json', methods=['POST'])
def route_json--- This code section failed: ---

 L.  56         0  SETUP_FINALLY        36  'to 36'

 L.  57         2  LOAD_GLOBAL              request
                4  LOAD_ATTR                get_json
                6  LOAD_CONST               False
                8  LOAD_CONST               True
               10  LOAD_CONST               False
               12  LOAD_CONST               ('force', 'silent', 'cache')
               14  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               16  STORE_FAST               'j'

 L.  58        18  LOAD_FAST                'j'
               20  LOAD_CONST               None
               22  COMPARE_OP               is-not
               24  POP_JUMP_IF_FALSE    32  'to 32'

 L.  59        26  POP_BLOCK        
               28  LOAD_STR                 'Valid JSON'
               30  RETURN_VALUE     
             32_0  COME_FROM            24  '24'
               32  POP_BLOCK        
               34  JUMP_FORWARD         48  'to 48'
             36_0  COME_FROM_FINALLY     0  '0'

 L.  60        36  POP_TOP          
               38  POP_TOP          
               40  POP_TOP          

 L.  61        42  POP_EXCEPT       
               44  JUMP_FORWARD         48  'to 48'
               46  END_FINALLY      
             48_0  COME_FROM            44  '44'
             48_1  COME_FROM            34  '34'

 L.  62        48  LOAD_STR                 'Not a valid JSON'
               50  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `LOAD_STR' instruction at offset 28


@app.route('/catch_me', methods=['PUT'])
def catch_me_1():
    if request.method == 'PUT':
        return redirect((url_for('catch_me_2')), code=307)
    res = Response('No')
    res.headers['Allow'] = 'PUT'
    return res


@app.route('/catch_me_2', methods=['PUT'])
def catch_me_2():
    if request.form.get('user_id') == '98':
        return redirect((url_for('catch_me_3')), code=307)
    return ('You are not user_id = 98', 401)


@app.route('/catch_me_3', methods=['PUT'])
def catch_me_3():
    if request.headers.get('Origin') == 'School':
        return 'You got me!'
    return ('You are not coming from School', 403)


@app.route('/route_100')
def route_100():
    return ('Route 100', 289)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)