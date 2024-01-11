import tkinter
from tkinter import ttk, Tk, StringVar

# Score list
score_individual = [15, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
score_relay = [30, 26, 24, 22, 20, 18, 16, 14, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# School list
schools = [
    "School_1",
    "School_2",
    "School_3",
    "School_4",
    "School_5",
    "School_6",
    "School_7",
    "School_8",
    "School_9",
    "School_10",
    "School_11",
    "School_12",
    "School_13",
    "School_14",
    "School_15",
    "School_16",
    "School_17",
    "School_18",
    "School_19",
    "School_20"
]

# Global variable
value = "I"
school_scores = dict()


def main():
    
    def click_button():
        global value
        value = v1.get()
        select_school()
    
    baseGround = Tk()
    baseGround.geometry("200x150")
    baseGround.title("Event")
    
    # Create and place main frame
    frame1 = ttk.Frame(baseGround)
    frame1.pack(fill = tkinter.BOTH, pady=20)
    
    # Style
    ttk.Style().theme_use("classic")
    
    # Label frame
    label_frame1 = ttk.Labelframe(
        frame1,
        text="Choose event",
        padding=(10),
        style="My.TLabelframe"
    )

    v1 = StringVar()        
    # Radiobutton 1
    rb1 = ttk.Radiobutton(
        label_frame1,
        text="Individual",
        value="I",
        variable=v1
    )
    # Radiobutton 2
    rb2 = ttk.Radiobutton(
        label_frame1, 
        text="Relay",
        value="R",
        variable=v1
    )
    
    # Button
    button12 = ttk.Button(
        frame1,
        text="OK",
        padding=(20, 5),
        command=click_button
    )
    
    # Layout
    frame1.grid()
    label_frame1.grid(row=0, column=0)
    rb1.grid(row=0, column=0) 
    rb2.grid(row=0, column=1) 
    button12.grid(row=1, pady=5)
    
    # Display
    baseGround.mainloop()
    

def select_school():
    
    global school_scores, value
    
    baseGround_new_csv = Tk()
    baseGround_new_csv.geometry("350x480")
    baseGround_new_csv.title("Caluculate scores")

    # Create and place main frame
    frame2 = ttk.Frame(baseGround_new_csv)
    frame2.pack(fill = tkinter.BOTH, pady=20)
    
    # Back to event screen
    def return_view():
        baseGround_new_csv.destroy()
    
    # Caluculate scores
    def caluculate(key, score):
        if key not in school_scores:
            school_scores[key] = score
        else:
            school_scores[key] += score
            
    def click_button():
        global school_scores
        school_scores = {}
        if value == "I":
            caluculate(cb1.get(), score_individual[0])
            caluculate(cb2.get(), score_individual[1])
            caluculate(cb3.get(), score_individual[2])
            caluculate(cb4.get(), score_individual[3])
            caluculate(cb5.get(), score_individual[4])
            caluculate(cb6.get(), score_individual[5])
            caluculate(cb7.get(), score_individual[6])
            caluculate(cb8.get(), score_individual[7])
            caluculate(cb9.get(), score_individual[8])
            caluculate(cb10.get(), score_individual[9])
            caluculate(cb11.get(), score_individual[10])
            caluculate(cb12.get(), score_individual[11])
            caluculate(cb13.get(), score_individual[12])
            caluculate(cb14.get(), score_individual[13])
            caluculate(cb15.get(), score_individual[14])
        elif value == "R":
            caluculate(cb1.get(), score_relay[0])
            caluculate(cb2.get(), score_relay[1])
            caluculate(cb3.get(), score_relay[2])
            caluculate(cb4.get(), score_relay[3])
            caluculate(cb5.get(), score_relay[4])
            caluculate(cb6.get(), score_relay[5])
            caluculate(cb7.get(), score_relay[6])
            caluculate(cb8.get(), score_relay[7])
            caluculate(cb9.get(), score_relay[8])
            caluculate(cb10.get(), score_relay[9])
            caluculate(cb11.get(), score_relay[10])
            caluculate(cb12.get(), score_relay[11])
            caluculate(cb13.get(), score_relay[12])
            caluculate(cb14.get(), score_relay[13])
            caluculate(cb15.get(), score_relay[14])
            caluculate(cb16.get(), score_relay[15])
            caluculate(cb17.get(), score_relay[16])
            caluculate(cb18.get(), score_relay[17])
            caluculate(cb19.get(), score_relay[18])
            caluculate(cb20.get(), score_relay[19])
        else:
            pass
        display_result()

    # Label frames and Comboboxes
    if value == "I" or value == "R":
        
        label_frame21 = ttk.Label(frame2, text="1st")
        label_frame21.grid(row=0, column=0)
        v1 = StringVar()
        cb1 = ttk.Combobox(frame2, textvariable=v1, values=schools, width=10)
        cb1.bind("<<ComboboxSelected>>", lambda e: print("v1=%s" % cb1.get()))
        cb1.grid(row=0, column=1)
        
        label_frame22 = ttk.Label(frame2, text="2nd")
        label_frame22.grid(row=1, column=0)
        v2 = StringVar()
        cb2 = ttk.Combobox(frame2, textvariable=v2, values=schools, width=10)
        cb2.bind("<<ComboboxSelected>>", lambda e: print("v2=%s" % cb2.get()))
        cb2.grid(row=1, column=1)
        
        label_frame23 = ttk.Label(frame2, text="3rd")
        label_frame23.grid(row=2, column=0)
        v3 = StringVar()
        cb3 = ttk.Combobox(frame2, textvariable=v3, values=schools, width=10)
        cb3.bind("<<ComboboxSelected>>", lambda e: print("v3=%s" % cb3.get()))
        cb3.grid(row=2, column=1)
        
        label_frame24 = ttk.Label(frame2, text="4th")
        label_frame24.grid(row=3, column=0)
        v4 = StringVar()
        cb4 = ttk.Combobox(frame2, textvariable=v4, values=schools, width=10)
        cb4.bind("<<ComboboxSelected>>", lambda e: print("v4=%s" % cb4.get()))
        cb4.grid(row=3, column=1)
        
        label_frame25 = ttk.Label(frame2, text="5th")
        label_frame25.grid(row=4, column=0)
        v5 = StringVar()
        cb5 = ttk.Combobox(frame2, textvariable=v5, values=schools, width=10)
        cb5.bind("<<ComboboxSelected>>", lambda e: print("v5=%s" % cb5.get()))
        cb5.grid(row=4, column=1)
        
        label_frame26 = ttk.Label(frame2, text="6th")
        label_frame26.grid(row=5, column=0)
        v6 = StringVar()
        cb6 = ttk.Combobox(frame2, textvariable=v6, values=schools, width=10)
        cb6.bind("<<ComboboxSelected>>", lambda e: print("v6=%s" % cb6.get()))
        cb6.grid(row=5, column=1)
        
        label_frame27 = ttk.Label(frame2, text="7th")
        label_frame27.grid(row=6, column=0)
        v7 = StringVar()
        cb7 = ttk.Combobox(frame2, textvariable=v7, values=schools, width=10)
        cb7.bind("<<ComboboxSelected>>", lambda e: print("v7=%s" % cb7.get()))
        cb7.grid(row=6, column=1)
        
        label_frame28 = ttk.Label(frame2, text="8th")
        label_frame28.grid(row=7, column=0)
        v8 = StringVar()
        cb8 = ttk.Combobox(frame2, textvariable=v8, values=schools, width=10)
        cb8.bind("<<ComboboxSelected>>", lambda e: print("v8=%s" % cb8.get()))
        cb8.grid(row=7, column=1)
        
        label_frame29 = ttk.Label(frame2, text="9th")
        label_frame29.grid(row=8, column=0)
        v9 = StringVar()
        cb9 = ttk.Combobox(frame2, textvariable=v9, values=schools, width=10)
        cb9.bind("<<ComboboxSelected>>", lambda e: print("v9=%s" % cb9.get()))
        cb9.grid(row=8, column=1)
        
        label_frame210 = ttk.Label(frame2, text="10th")
        label_frame210.grid(row=9, column=0)
        v10 = StringVar()
        cb10 = ttk.Combobox(frame2, textvariable=v10, values=schools, width=10)
        cb10.bind("<<ComboboxSelected>>", lambda e: print("v10=%s" % cb10.get()))
        cb10.grid(row=9, column=1)
        
        label_frame211 = ttk.Label(frame2, text="11th")
        label_frame211.grid(row=10, column=0)
        v11 = StringVar()
        cb11 = ttk.Combobox(frame2, textvariable=v11, values=schools, width=10)
        cb11.bind("<<ComboboxSelected>>", lambda e: print("v11=%s" % cb11.get()))
        cb11.grid(row=10, column=1)
        
        label_frame212 = ttk.Label(frame2, text="12th")
        label_frame212.grid(row=11, column=0)
        v12 = StringVar()
        cb12 = ttk.Combobox(frame2, textvariable=v12, values=schools, width=10)
        cb12.bind("<<ComboboxSelected>>", lambda e: print("v12=%s" % cb12.get()))
        cb12.grid(row=11, column=1)
        
        label_frame213 = ttk.Label(frame2, text="13th")
        label_frame213.grid(row=12, column=0)
        v13 = StringVar()
        cb13 = ttk.Combobox(frame2, textvariable=v13, values=schools, width=10)
        cb13.bind("<<ComboboxSelected>>", lambda e: print("v13=%s" % cb13.get()))
        cb13.grid(row=12, column=1)
        
        label_frame214 = ttk.Label(frame2, text="14th")
        label_frame214.grid(row=13, column=0)
        v14 = StringVar()
        cb14 = ttk.Combobox(frame2, textvariable=v14, values=schools, width=10)
        cb14.bind("<<ComboboxSelected>>", lambda e: print("v14=%s" % cb14.get()))
        cb14.grid(row=13, column=1)
        
        label_frame215 = ttk.Label(frame2, text="15th")
        label_frame215.grid(row=14, column=0)
        v15 = StringVar()
        cb15 = ttk.Combobox(frame2, textvariable=v15, values=schools, width=10)
        cb15.bind("<<ComboboxSelected>>", lambda e: print("v15=%s" % cb15.get()))
        cb15.grid(row=14, column=1)
    
    if value == "R":

        label_frame216 = ttk.Label(frame2, text="16th")
        label_frame216.grid(row=15, column=0)
        v16 = StringVar()
        cb16 = ttk.Combobox(frame2, textvariable=v16, values=schools, width=10)
        cb16.bind("<<ComboboxSelected>>", lambda e: print("v16=%s" % cb16.get()))
        cb16.grid(row=15, column=1)
        
        label_frame217 = ttk.Label(frame2, text="17th")
        label_frame217.grid(row=16, column=0)
        v17 = StringVar()
        cb17 = ttk.Combobox(frame2, textvariable=v17, values=schools, width=10)
        cb17.bind("<<ComboboxSelected>>", lambda e: print("v17=%s" % cb17.get()))
        cb17.grid(row=16, column=1)
        
        label_frame218 = ttk.Label(frame2, text="18th")
        label_frame218.grid(row=17, column=0)
        v18 = StringVar()
        cb18 = ttk.Combobox(frame2, textvariable=v18, values=schools, width=10)
        cb18.bind("<<ComboboxSelected>>", lambda e: print("v18=%s" % cb18.get()))
        cb18.grid(row=17, column=1)

        label_frame219 = ttk.Label(frame2, text="19th")
        label_frame219.grid(row=18, column=0)
        v19 = StringVar()
        cb19 = ttk.Combobox(frame2, textvariable=v19, values=schools, width=10)
        cb19.bind("<<ComboboxSelected>>", lambda e: print("v19=%s" % cb19.get()))
        cb19.grid(row=18, column=1)
        
        label_frame220 = ttk.Label(frame2, text="20th")
        label_frame220.grid(row=19, column=0)
        v20 = StringVar()
        cb20 = ttk.Combobox(frame2, textvariable=v20, values=schools, width=10)
        cb20.bind("<<ComboboxSelected>>", lambda e: print("v20=%s" % cb20.get()))
        cb20.grid(row=19, column=1)
        
    # Button
    button = ttk.Button(
        baseGround_new_csv,
        text="Caluculate!",
        command=click_button
    )
    button.place(x=150, y=50)
    
    # Back button
    btn_return = ttk.Button(
        baseGround_new_csv, 
        text="Back to the previous screen", 
        command=return_view
    )
    btn_return.place(x=150, y=80)
    
    baseGround_new_csv.mainloop()
    
    
def display_result():
    
    global school_scores
    
    # Back to event screen
    def return_view():
        baseGround_new_csv.destroy()
        
    baseGround_new_csv = Tk()
    baseGround_new_csv.geometry("280x425")
    baseGround_new_csv.title("Result of the scores")
    
    # Print the result
    i = 0
    for key, score in school_scores.items():
        lbl_result1 = ttk.Label(baseGround_new_csv, text="School: " + key + "  ")
        lbl_result1.grid(row=i, column=0, sticky=tkinter.W)
        lbl_result2 = ttk.Label(baseGround_new_csv, text="Score: " + str(score))
        lbl_result2.grid(row=i, column=1, sticky=tkinter.W)
        i += 1
    
    # Back button
    btn_return = ttk.Button(
        baseGround_new_csv, 
        text="Back to the previous screen", 
        command=return_view
    )
    btn_return.place(x=50, y=390)
    
    baseGround_new_csv.mainloop()
    
    
if __name__ == "__main__":
    main()
