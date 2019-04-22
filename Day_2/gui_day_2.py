import tkinter as tk
from tkinter import messagebox


def click_me():
    messagebox.showinfo('Click Event', 'You have clicked, Good Work')


def create_labels(window):
    new_label = tk.Label(window, text='I am a Label, made of text. ')
    new_label.pack()
    next_label = tk.Label(window, text='I am also a label, what about me?')
    next_label.pack()


def create_buttons(window):
    the_button = tk.Button(window, text='This is our first Button', command=click_me)
    the_button.pack()


def create_image(window):
    the_image = tk.PhotoImage(file='fractal.gif')
    fractal_label = tk.Label(window, image=the_image)
    fractal_label.image = the_image
    fractal_label.pack()


def frame_click():
    if messagebox.askyesno('Click Event', 'You have clicked, Good Work') == tk.YES:
        messagebox.showinfo('Message Box', 'You have clicked yes!')



def create_frame(window):
    frame = tk.Frame(window, background='blue')
    label_in_frame = tk.Label(frame, text='This label will be in the frame, above the button',
                              background='tomato2')
    button_in_frame = tk.Button(frame, text='This button is in the Frame', command=frame_click)

    label_in_frame.pack()
    button_in_frame.pack()
    frame.pack()


main_window = tk.Tk()
main_window.title('This is the Title String')
main_window.geometry('800x500')
create_labels(main_window)
create_buttons(main_window)
create_image(main_window)
create_frame(main_window)
main_window.mainloop()
