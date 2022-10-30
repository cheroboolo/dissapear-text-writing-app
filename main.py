from tkinter import *

BACKGROUND_COLOR = "#9BA17B"
COLOR = "#FAD6A5"

count = 0


#function that delete our entire text and add empty ""
def disappear_text():
    text.delete(1.0, END)
    text.insert(END, "")


#trigger function to compare equilent text is the same or there changes to add new text.
#if there is no change and data is same, then we are inactive and timer starts count seconds before trigger
# dissapear_text function
def check_disappear():
    global count, text_data
    if text_data == text.get(1.0, END):
        if count == 5:
            window.after(1000, disappear_text)
            count = -1
        window.after(1000, check_disappear)
        count += 1
        time_label.config(text=f"{count} Seconds")
    else:
        window.after(1000, check_disappear)
        text_data = text.get(1.0, END)
        count = 0


#create window
window = Tk()
window.title("Text Writing APP")
window.config(padx=100, pady=100, bg=BACKGROUND_COLOR)

#labels
title_label = Label(text="Welcome to Writing Text Disappear app", bg=BACKGROUND_COLOR, fg=COLOR, font=("Helvetica", 30), highlightthickness=0)
title_label.grid(column=0, row=0, pady=20)

label = Label(text="Type some text", font=("Helvetica", 20), bg=BACKGROUND_COLOR, highlightthickness=0)
label.grid(column=0, row=1)

time_label = Label(text="0 Seconds", font=("Helvetica", 20), bg=BACKGROUND_COLOR, highlightthickness=0)
time_label.grid(column=0, row=3)

#text field
text_data = ""
text = Text(width=50, height=20, font=("Helvetica", 20), bg=BACKGROUND_COLOR, highlightthickness=0)
text.grid(column=0, row=2)
#pointer start with typing
text.focus()

#every second timer starts checking conditions in check_disappear function
window.after(1000, check_disappear)

window.mainloop()
