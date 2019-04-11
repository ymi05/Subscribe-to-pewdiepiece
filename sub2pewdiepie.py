import webbrowser
from tkinter import *
root = Tk() #kinter class which creates a blank window
#####################################################
def subscirbe_PEWDIEPIE():
    webbrowser.open(channel_link) #opens the site
#####################################################

label_1 = Label(root,text = 'Subscribe to Pewdiepie!!!!') 
label_1.grid(row = 0)#where on the grid do you wnna put iT 

channel_link= ("https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw?sub_confirmation=1")
sub_button = Button(root,text="Click to Subscribe now",command =subscirbe_PEWDIEPIE,bg='red')#whenever i click run
sub_button.grid(columnspan=10)



root.mainloop()