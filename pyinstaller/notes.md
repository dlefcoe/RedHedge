# pyinstaller by DL
Written by @dlefcoe

## first install
    pip install pyinstaller


## now create a python file
you can just make a simple hello world file for this

    x = 'hello world'
    print(x)
    
    y = input('press ENTER to exit')


## save the file
save the file as **helloworld.py**


## now run the installer
There are 2 methods for this.

1. distribution
2. onefile

### distributiuon
just run as normal (in the example for helloworld.py)

    pyinstaller helloworld.py

### onefile
run using the hello --onefile option
    pyinstaller --onefile helloworld.py
    
if you have a gui then also inclue the -w option so that the console does not remain open in the background

    pyinstaller --onefile -w helloworld.py


The end.
