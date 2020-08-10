from jinja2 import Environment, FileSystemLoader
import sys
import os

#
# sys.argv is list of files to include
#

file_loader = FileSystemLoader('./templates')
env = Environment(loader=file_loader)
template = env.get_template('items.xml')

paths = [os.path.sep + os.path.sep.join(x.split(os.path.sep)[1:]) for x in sys.argv[1:]]

objs = []
for fpath in paths:
    directory, fname = os.path.split(fpath)
    objs.append({'path':fpath, 'fname':fname})

output = template.render(objects = objs, title="Test Import", course="crs")

f = open('./output/exportAssessment.xml','w')
f.write(output)
f.close()

template = env.get_template('manifest.xml')
output = template.render(objects = objs)

f = open('./output/imsmanifest.xml','w')
f.write(output)
f.close()

