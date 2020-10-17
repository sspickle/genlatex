from jinja2 import Environment, FileSystemLoader
import sys
import os

#
# sys.argv is list of files to include
#

istart = 2168671

file_loader = FileSystemLoader('./templates')

env = Environment(loader=file_loader)
template = env.get_template('items.xml')

print(sys.argv[1:])

#paths = [os.path.sep + os.path.sep.join(x.split(os.path.sep)[1:]) for x in sys.argv[1:]]
paths = [os.path.sep.join(x.split(os.path.sep)[1:]) for x in sys.argv[1:]]

print (paths)

objs = []
counter = 0

for fpath in paths:
    counter += 1
    directory, fname = os.path.split(fpath)
    objs.append({'path':fpath, 'fname':fname, 'ident':istart + counter})

output = template.render(objects = objs, title="Pool Import", course="crs")

f = open('./output/exportAssessment.xml','w')
f.write(output)
f.close()

template = env.get_template('manifest.xml')
output = template.render(objects = objs)

f = open('./output/imsmanifest.xml','w')
f.write(output)
f.close()
