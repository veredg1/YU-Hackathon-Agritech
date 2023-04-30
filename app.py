import tkinter
from tkinter import Tk

from graph import Graph
from graph import NodeBody
from localstore import NodeBody


top: Tk = tkinter.Tk()
Graph = Graph()
start = tkinter.Button(top, text= "create account", command = Graph.insert(NodeBody( 'ip',1, dict(), dict(), list, list )))
start.pack()

start.mainloop()
top.mainloop()
