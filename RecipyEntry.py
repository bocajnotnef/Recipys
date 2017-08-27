#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import tkinter

def Format(ing_list, inst_list, title, serves):
    f_text = [title]
    f_text.append(("=" * len(title)) + '\n')

    f_text.append("Ingredients")
    f_text.append("-----------\n")
    for ing in ing_list:
        if ing == "": continue
        f_text.append("* " + ing)

    f_text.append('\n')

    f_text.append("Instructions")
    f_text.append("------------\n")

    for inst in inst_list:
        if inst == "": continue
        f_text.append("#. " + inst)

    f_text.append('\n')

    f_text.append("Serves: " + serves + '\n')

    f_text.append("Notes")
    f_text.append("-----")
    f_text.append('*\n*\n')
    f_text.append("Additional Links")
    f_text.append("----------------")

    return f_text


class simpleapp_tk(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def ProcessData(self, raw_data):
        data = raw_data.split('\n')
        return data


    def WriteToFile(self):
        ing_data = self.ing_box.get("1.0",'end-1c')
        inst_data = self.inst_box.get("1.0",'end-1c')
        title = self.r_name.get()
        serves = self.servings.get()

        if title == "": title = "Recipe"

        ing_list = self.ProcessData(ing_data)
        inst_list = self.ProcessData(inst_data)

        f_text = Format(ing_list, inst_list, title, serves)

        temp = title.lower().split(' ')
        filename = ""
        for word in temp: filename += (word + "-")
        filename = filename[:-1] + ".rst"

        _file = open(filename, 'w')

        for line in f_text:
            _file.write(line + '\n')

        _file.close()

        success = tkinter.Label(text=filename + " was created successfully!")
        success.grid(row=6, column=1)

    def initialize(self):
        self.grid()
        self.geometry("800x1000")

        title_label = tkinter.Label(text="Title of Dish: ", anchor="w")
        self.r_name = tkinter.Entry()
        ing_label = tkinter.Label(text="Enter Ingredients Below (put each Ingredient on a new line)")
        self.ing_box = tkinter.Text()
        inst_label = tkinter.Label(text="Enter Instructions Below (put each Instruction on a new line)")
        self.inst_box = tkinter.Text()
        serve_label = tkinter.Label(text="Serves: ", anchor="w")
        self.servings = tkinter.Entry()

        create_button = tkinter.Button(self, text=u"Create File", command=self.WriteToFile)
        exit_button = tkinter.Button(self, text=u"Exit", command=self.quit)

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(2, weight=2)
        title_label.grid(row=0, column=0)
        self.r_name.grid(row=0, column=1, ipadx=50, pady=10, sticky=tkinter.W)
        ing_label.grid(row=1, column=1)
        self.ing_box.grid(row=2, column=1, pady=10)
        inst_label.grid(row=3, column=1)
        self.inst_box.grid(row=4, column=1, pady=10)
        serve_label.grid(row=5, column=0)
        self.servings.grid(row=5, column=1, ipadx=50, pady=10, sticky=tkinter.W)
        create_button.grid(row=6, column=0)
        exit_button.grid(row=6, column=2, padx=20)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('RecipyEntry')
    app.mainloop()
