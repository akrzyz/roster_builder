from tkinter import *
from tkinter.ttk import *
from GridOfWidgets import *
import gui_game_selector as QQQ

class Application(Frame):
    def say_hi(self, event = None):
        print("hi there, everyone!")
        #self.hi_there.pack_forget();

    def addButombToNet(self):
        self.WGreed.appendRow([Button(self.WGreed,text="buton1"),Button(self.WGreed,text="buton1")])
        
    def delRow(self):
        row_n = len(self.WGreed.getGrid());
        if row_n > 0:
            self.WGreed.detachRow(row_n - 1);
    def foo(self,e):
        print('selected: ' + self.cb_var.get())
        print(type(e))
        
    def set_dial(self):
        root = self;
        engine = QQQ.b_engine();
        b = QQQ.Builder_game_selector(engine, None)
        print(b.go())
        #wait_wondow(b)
        print('end action')
        
    def createWidgets(self):
        #button quit
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})
        
        #button dial
        self.dial = Button(self)
        self.dial["text"] = "dial"
        self.dial["command"] =  self.set_dial
        self.dial.pack({"side": "left"})
        
        #button say hello
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack({"side": "left"})
        
        #combobox
        self.cb_var = StringVar()
        self.c_b = Combobox(self, textvariable=self.cb_var, state='readonly')
        self.c_b['values'] = ('USA', 'Canada', 'Australia')
        self.c_b.current(0)
        self.c_b.bind('<<ComboboxSelected>>', self.foo) 
        self.c_b.pack({"side": "left"})        
        
        #button addButombToNet
        self.bAdd = Button(self,text="add row",command=self.addButombToNet);
        self.bAdd.pack();

        #button delRow
        self.bDel = Button(self,text="del row",command=self.delRow);
        self.bDel.pack();
        
        #mygreed
        self.WGreed = WidgetsGrid(self);
        self.WGreed['borderwidth'] = 2;
        self.WGreed['relief'] = 'groove';
        self.WGreed.pack({"side": "top"})
        
        #tree
        self.tree = Treeview(self)
        self.tree.pack()
        self.tree.insert('', 'end', 'widgets', text='Widget Tour')
        self.tree.insert('', 0, 'gallery', text='Applications')
        id = self.tree.insert('', 'end', text='Tutorial')
        self.tree.insert('widgets', 'end', text='Canvas')
        self.tree.insert(id, 'end', text='Tree')
        self.tree.move('widgets', 'gallery', 'end')
        
        self.tree.item('gallery', open=TRUE)
        isopen = self.tree.item('widgets', 'open')
        
        #self.tree.bind('<Double-Button-1>', self.say_hi)
        self.tree.tag_bind('widgets', '<Double-Button-1>', self.say_hi)

        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()