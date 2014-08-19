import tkinter

tk = tkinter

def main():

    base = tk.Tk()
    base.title("HTML Code Maker")

    panel = tk.Canvas(base, width=600, height=600)
    panel.pack(side= tk.LEFT)

    frame = tk.Frame(base)
    frame.pack(side = tk.RIGHT)
    
   
    textVar = tk.StringVar()
    textVar.set('Enter Text Here')
    htmltext = tk.Entry(frame,textvariable=textVar)
    htmltext.pack()
   
   
    
    
    
    def goHandler():
        file = open('NewWebPage.html', 'w')

        text = "<html>\n<body>\n" + str(textVar.get()) + "\n</body>\n</html>"

        file.write(text)
        file.close()
    
    goButton = tk.Button(frame,text='Go', command = goHandler)
    goButton.pack()


    

    
    
    
    
    tk.mainloop()
    

if __name__ == "__main__":
    main()













