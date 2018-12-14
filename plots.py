'''
README!!!

To use img2pdf you will likely have to install it using pip; navigate to
pip (default location for Anaconda is User/your_username/AppData/Continuum/
Anaconda3/Scripts) in the command line and run "pip install img2pdf"

Make sure all subfigures are closed before calling this script as the images
will get plotted on top of one another and it creates a mess

Seriously, README!!!
'''

import os
import img2pdf

exec(open('./detection.py').read())
exec(open('./power.py').read())
exec(open('./time.py').read())

with open("plots.pdf", "wb") as f: # throws every .jpg into a pdf
    f.write(img2pdf.convert([i for i in
    os.listdir('C:\\Users\\kburkhardt3\\Documents\\RPE_data')
    if i.endswith(".jpg")]))