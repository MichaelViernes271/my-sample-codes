import tkinter

window = tkinter.Tk()
window.title("Calculator")
window_frame = tkinter.Frame(window, borderwidth=2)

window_frame.pack(fill="x", expand=1)
led_display = tkinter.Entry(window_frame, text="0")
clr_button = tkinter.Button(window_frame, text="CLR")
clr_button.pack()
window.mainloop()