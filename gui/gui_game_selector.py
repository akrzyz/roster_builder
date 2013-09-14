from tkinter import *
from tkinter.ttk import *
#from tkinter.dialog import as dial
import tkinter.simpledialog as dial
from b_engine import *
from b_classes import *
from b_xmlreader import *
import PyDial as WWW

class Builder_game_selector(Frame):
    
    def createWidgets(self):
        #strVariable
        self.game = StringVar()
        self.army = StringVar() 
      
        #internal Panels
        self.game_panel = Labelframe(self, text='Game:')
        self.game_panel.grid(column=0, row=0, sticky=(W,N,E), padx=3, pady=3);
        self.army_panel = Labelframe(self, text='Army:')
        self.army_panel.grid(column=0, row=1, sticky=(W,N,E), padx=3, pady=3);
        
        self.cb_game = Combobox(self.game_panel, textvariable=self.game, state='readonly')
        self.cb_army = Combobox(self.army_panel, textvariable=self.army, state='readonly')
        self.ok_button = Button(self)
        
        #init game
        self.get_games()
        #init combobox game                
        self.cb_game['values'] = self.games_list
        self.cb_game.current(0)
        self.cb_game.bind('<<ComboboxSelected>>', self.set_game) 
        self.cb_game.grid(column=0, row=0 , sticky=(W,N,E), padx=3, pady=3);
        #set game and init game
        self.game.set(self.cb_game.get())
        self.set_game()
        
        self.get_armies()
        #init combobox army       
        self.cb_army['values'] = self.army_list
        self.cb_army.current(0)
        self.cb_army.grid(column=0, row=0 , sticky=(W,N,E), padx=3, pady=3);
        self.army.set(self.cb_army.get())
        
        #admit button        
        self.ok_button["text"] = "ok",
        self.ok_button["command"] = self.ok_call_back
        self.ok_button.grid(column=0, row=2, sticky=(W,N,E), padx=3, pady=3);
    
    def ok_call_back(self):
        self.quit()
        return (self.game.get(), self.army.get())

    
    def admition_state(self,state):
        if(state):
            self.cb_army['state']='readonly'
            if self.cb_army.get() == '----' : self.cb_army.current(0)
            self.ok_button['state']='enabled'
        else:
            self.cb_army['state']='disabled'
            self.cb_army.set('----')
            self.ok_button['state']='disabled'
            
    
    def set_game(self,event=None):
        self.engine.init_game(self.game.get())
        self.get_armies()
        
    def get_games(self):
        self.games_list = []
        if self.engine.config != None :
            for game in self.engine.config:
                self.games_list.append(game['name'])
            self.admition_state(True)
        else:
            self.admition_state(False)

    def get_armies(self):        
        self.army_list = []
        if self.engine.game_config != None :
            for army in self.engine.game_config.keys() :
                self.army_list.append(army)
            self.admition_state(True)
        else:
            self.admition_state(False)
            
    def __init__(self, engine, master=None):        
        Frame.__init__(self, master)
        self.engine = engine
        self.pack()
        self.createWidgets()
        self.master = master
        
        
    def go(self):
        self.master.grab_set()
        self.master.mainloop()
        self.master.destroy()#quit()
        return None
        
if __name__ == '__main__' :
    root = Tk()
    root.title('Builder')
    engine = b_engine();
    app = Builder_game_selector(engine,root)
    print(app.go())
    root.mainloop()
    root.quit()
    print(type(engine))
    print(engine.config)
    print(engine.game_config)