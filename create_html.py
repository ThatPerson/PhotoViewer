import json
import sys
import os

filename = "pics.json" # File containing list of information.

start = '<!doctype html><html><head><title>Photo Album</title><link rel="stylesheet" href="style.css"></head><body><div class="container">'

end = '</div></body></html>'


def gen_imagesrc(d, l):
	""" Produces the HTML code for that set of images.
		d is a dict containing the name, date, location, directory, and 
		list of pictures. l is 1 if this is a sub page, and 0 if this is 
		home. """
	name = d['name']
	date = d['date']
	location = d['location']
	directory = d['directory']
	files = d['pics']
	if (l == 1):
		p = '<a class="nav" href="index.html">Go Home</a>'
	else:
		p = '<a class="nav" href="'+directory+'.html">Go to page</a>'
	srcd = '<div class="image_set"><div class="left"><h2 class="title">'+name+'</h2><p class="date">'+date+'</p><p class="location">'+location+'</p>'+p+'</div><div class="images">'
	for i in files:
		srcd = srcd + '<a href="'+directory+'/original/'+i+'"><img src="'+directory+'/final/'+i+'" class="img"/></a>'
	scrd = srcd + '</div></div>'
	return scrd
    

with open(filename, "r") as f:
	data = json.load(f)
    
	print(len(data['p']))
	source = start
	for i in range(len(data['p']) - 1, -1, -1):

		short_source = start + gen_imagesrc(data['p'][i], 1) + end
		with open(data['p'][i]['directory'] + ".html", "w") as f:
			f.write(short_source)
	
	
		print(i)
		print(gen_imagesrc(data['p'][i], 1))
		source = source + gen_imagesrc(data['p'][i], 0)
	source = source + end
	
with open('index.html', 'w') as f:
	f.write(source)
