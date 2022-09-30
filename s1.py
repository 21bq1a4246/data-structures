try:
    fname=input('enter file name:')
    fp=open(fname)
    print('contents are \n',fp.read())
except FileNotFoundError:
    print(fname+'not exist')
finally:
    fp.close()
    print('file closed')