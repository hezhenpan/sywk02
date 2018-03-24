#!/usr/bin/env python3
# *_* coding:utf-8 *_*

from flask import Flask
from flask import *
import os
import json 

app = Flask(__name__)


@app.route('/')
def index():
	flist = os.listdir('/home/shiyanlou/files/')
	dictlist = []
	for x in flist:
		with open('/home/shiyanlou/files/'+x, 'r') as ff:
			dictlist.append(json.loads(ff.read()))


	return render_template('index.html', js1=dictlist[0], js2=dictlist[1])



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404



@app.route('/files/<filename>')
def file(filename):
	flist = os.listdir('/home/shiyanlou/files/')
	if filename+'.json' not in flist:
		abort(404)
	with open('/home/shiyanlou/files/'+filename+'.json', 'r') as ff:
		print('/home/shiyanlou/files/'+filename+'.json')
		dd1 = json.loads(ff.read())

	return render_template('file.html', jsdict = dd1)









