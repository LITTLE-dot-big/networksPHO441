This is a program to analyse the spread of disease using biological networks.
SECIR model of disease transmission is assumed in this program.
It is written in Python 3.7

Modules required:
    1. Eon
    2. networks
    3. collections
    4. matplotlib
    5. cv2 (OpenCV)

This program first creates a graph, on which all the nodes(=1oooo) are situated. 
The rate at which one individual goes from one state into another is passed into the program using the trackbars.
An initial number of 5000 individuals are assumed to be susceptible.
Then all the values are plotted against time(from 0 to infinity). 


'test0.py' program gives an example of how edges are added into the graph
'test1.py' and 'test3.py' programs are small scale examples of 'main.py' which takes only one set of values.