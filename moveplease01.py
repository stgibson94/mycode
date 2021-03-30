#!/usr/bin/env python3

# imports
import shutil
import os

# start at dir
os.chdir('/home/student/mycode/')

# move a file
shutil.move('raynor.obj', 'ceph_storage/')

# prompt user for file rename
xname = input('What is the new name for kerrigan.obj? ')

# move a file and rename
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
