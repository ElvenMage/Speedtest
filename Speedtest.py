import speedtest
from tkinter import *

root = Tk()
root.title("Speedtest")
canvas = Canvas(
    root,
    width=600,
    height=600
    )

canvas.pack()
# Functions


def testspeed():
    speed = speedtest.Speedtest()
    root.title("Testing...")
    download_text = str(round(speed.download())/1000/1000) + " Mbps"
    upload_text = str(round(speed.upload())/1000/1000) + " Mbps"
    download_label.config(text=download_text)
    upload_label.config(text=upload_text)
    root.title("Speedtest")


# Button
speedtest_button = Button(
    root,
    text="Test",
    bg="Blue",
    fg="Black",
    padx=22,
    pady=5,
    font=("Arial", 15),
    command=testspeed
)
# Labels
download_label = Label(
    root,
    font=("Arial", 15)
    )

upload_label = Label(root,
                     font=("Arial", 15)
                     )

canvas.create_window(300,
                     290,
                     window=speedtest_button
                     )

canvas.create_window(170,
                     120,
                     window=download_label
                     )

canvas.create_window(440,
                     120,
                     window=upload_label
                     )

root.mainloop()
