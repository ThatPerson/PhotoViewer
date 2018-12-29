# PhotoViewer
Set of scripts to take folders of images and turn them into a website.

To use, place images into folders in the following format (for folder 'NAME');

'''NAME/original/*JPG'''

Run shrink.sh on this

'''./shrink.sh NAME'''

Then generate the json file

'''python3 gen.py'''

Fill out the directory name, images name. 

Then run

'''python3 create_html.py'''

And the output is in index.html. 
