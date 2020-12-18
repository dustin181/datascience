import os

#get current working directory
os.getcwd()

#change working directory
os.chdir('C:\\Python33')

os.listdir()
os.listdir('G:\\')
os.mkdir('test')
os.rename('test','new_one')
os.remove('old.txt')
os.rmdir('new_one')

#remove non-empty directory
import shutil
shutil.rmtree('test')




