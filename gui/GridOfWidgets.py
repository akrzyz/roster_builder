from tkinter import *

class WidgetsGrid(Frame):

    #constuctor
    def __init__(self, master=None, columns=0, rows=0):
        Frame.__init__(self, master);
        self.widgetsGrid = [[None]*columns]*rows;
    
    #getNet() rerurn net with widgets
    def getGrid(self):
        return self.widgetsGrid;

    #getRow(index) return row with widgets form net 
    def getRow(self, index):
        try:
            r_index = self.widgetsGrid[index]
        except:
            r_index = None
            pass
        return r_index;
        
    #appendRow([widgets...]) append row of widgets to net
    def appendRow(self, row):
        self.widgetsGrid.append(row);
        for i,widget in enumerate(row) :
            widget.grid(column=i, row=len(self.widgetsGrid)-1 , sticky=(W,N), padx=1, pady=1);

    #detachRow(index) detach row of widgets        
    def detachRow(self, index):
        try:
            for widget in self.widgetsGrid[index]: 
                widget.grid_forget();
                widget.destroy();
            del self.widgetsGrid[index];
        except:
            pass;
        