import tkinter as tk
import pybase64
from PIL import Image, ImageTk
from tkinter import messagebox

window = tk.Tk()
window.title("Secret Notes")
image= ImageTk.PhotoImage(Image.open('topsecret3.png'))

label_image = tk.Label(window,image=image)
label_image.pack()
#text dosyasını oluşturma
#f = open("mythinking.txt", "w")

def button_clicked():
    titleValue=[]
    secret=[]
    master_key_value=[]
    #print(titleValue)
    #get text from text box
    title_value = entry1.get()
    secret = textarea.get(1.0, "end-1c")
    #clear the text box
    entry1.delete(0, 'end')
    textarea.delete(1.0,"end-1c")
    #Logic for password
    if not title_value or not secret:
        messagebox.showwarning("Warning", "Title and secret cannot be empty!")
        return
    if entry2.get() == "password":
        #convert to byte
        secret = secret.encode("ascii")
        #convert to base64
        secret = pybase64.b64encode(secret)
        #convert it back ascii
        secret = secret.decode("ascii")
        #print to text box
        textarea.insert("end-1c", secret)
        f = open("mythinking.txt", 'a')
        f.write(f"{title_value}:\n {secret}\n")
        f.close()
    else:
        #yanlış master key girilirse çıkacak.
        messagebox.showwarning("Incorrect!","Incorrect master key,Try again or leave!")


def button_clicked2():
    # get text from text box
    secret = textarea.get(1.0, "end-1c")
    # clear the text box
    textarea.delete(1.0, "end-1c")
    # Logic for password
    if entry2.get() == "aspectar":
        # convert to byte
        secret = secret.encode("ascii")
        # convert it back base64
        secret = pybase64.b64decode(secret)
        # convert it back ascii
        secret = secret.decode("ascii")
        # print to text box
        textarea.insert("end-1c", secret)
    else:
        # yanlış master key girilirse çıkacak.
        messagebox.showwarning("Incorrect!", "Incorrect master key,Try again or leave!")




    return
label1 = tk.Label(text="Enter Your Title")
label1.pack()

entry1 = tk.Entry()
entry1.pack()

label2 = tk.Label(text="Enter your secret")
label2.pack()

textarea= tk.Text(width=50,height=10)
textarea.pack()

label3 = tk.Label(text="Enter master key")
label3.pack()

entry2 = tk.Entry(show="*")
entry2.pack()

button1 = tk.Button(text= "Save & Encrypt",command=button_clicked)
button1.pack()

button2 = tk.Button(text= "Decrypt",command=button_clicked2)  ###()bu işaret verildiğinde buton tıklanmış sayılıyordu. ()'nu nerede kullanıp nerede kullanmyacağımızı anlamak için iyi bir yol...
button2.pack()

window.mainloop()