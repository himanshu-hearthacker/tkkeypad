import Tkinter
from Tkinter import Entry


def main():
    root = Tkinter.Tk()
    numpad = NumPad(root)
    root.mainloop()
btn_list = [
            '1','2','3','Del',
            '4','5','6','End',
            '7','8','9','Text',
            '#','0','*','Call']

class NumPad(Tkinter.Frame):
    def __init__(self, root):
        Tkinter.Frame.__init__(self, root)
        self.grid()
        self.numpad_create()
        Entry = Tkinter.Entry(width= 30,bd=5)
        Entry.grid(row=6, columnspan=4, rowspan=1)
    def numpad_create(self):
        r = 0
        c = 0
        for b in btn_list:
            #cmd = lambda: print(b)
            self.b= Tkinter.Button(self, text=b,width=5,command= self.cmd).grid(row=r,column=c)
            print(b)
            c += 1
            if c > 3:
                c = 0
                r += 1
    #def Entry():
        #Entry = Tkinter.Entry
        #Entry.insert()
        #self.call = self.call + 1
    def cmd(self):
        if row == 0 and column == 0:
            Entry.insert ("1")
        else:
            print(nope)

        #Entry.insert(20,"1")
        #e = Entry()
        #e.insert(0,"number")
        #print("b")

        
main()
