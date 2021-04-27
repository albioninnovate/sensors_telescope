from graphviz import Source

"""
This is a viewer for ".dot" files.  Opens new window with diagram and writes the image to disk.
To use, change file name and output format if needed. 

ref: https://graphviz.org/

"""
filename = 'test.dot'

s = Source.from_file('test.dot', format='png')
s.view()
