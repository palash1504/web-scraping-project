from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
from PIL import ImageTk, Image
import os

def scrape():
    root = Tk()
    root.title("Web Scraper")
    root.geometry("800x370")

    img = image.resize((180, 70))

    my_img = ImageTk.PhotoImage(img)
    w = Label(root, text='', font=('Times', 6))
    w.pack()
    label = Label(root, image=my_img)
    label.pack()

    url = link_n
    response = requests.get(url)
    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent, "html.parser")
    # print(soup.prettify)

    products = []
    prices = []
    ratings = []
    #product = soup.find('div', attrs={'class': '_4rR01T'})
    #print(product.text)
    for a in soup.findAll('a', href=True, attrs={'class': '_1fQZEK'}):
        name = a.find('div', attrs={'class': '_4rR01T'})
        price = a.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
        rating = a.find('div', attrs={'class': '_3LWZlK'})
        p1 = price.text
        p2 = p1.lstrip("₹")
        p2 = "Rs. " + p2
        products.append(name.text)
        prices.append(p2)
        ratings.append(rating.text)

    path = "C:/Users/acer/Desktop/mini_final/"
    path = path+file_name

    # Check whether a path pointing to a file
    isFile = os.path.isfile(path)

    if isFile == False:
        df = pd.DataFrame({'Product Name': products, 'Prices': prices, 'Ratings': ratings})
        df.head()
        df.to_csv(file_name, mode='a', index=False)
    else:
        df = pd.DataFrame({'Product Name': products, 'Prices': prices, 'Ratings': ratings})
        df.to_csv(file_name, mode='a', index=False, header=False)

    for i in range(2, 11):
        url = link_n + "page=" + str(i)
        response = requests.get(url)
        htmlcontent = response.content
        soup = BeautifulSoup(htmlcontent, "html.parser")
        # print(soup.prettify)

        products = []
        prices = []
        ratings = []
        product = soup.find('div', attrs={'class': '_4rR01T'})
        # print(product.text)
        for a in soup.findAll('a', href=True, attrs={'class': '_1fQZEK'}):
            name = a.find('div', attrs={'class': '_4rR01T'})
            price = a.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
            rating = a.find('div', attrs={'class': '_3LWZlK'})
            p1 = price.text
            p2 = p1.lstrip("₹")
            p2 = "Rs. " + p2
            products.append(name.text)
            prices.append(p2)
            ratings.append(rating.text)

        path = "C:/Users/acer/Desktop/mini_final/"
        path = path + file_name

        # Check whether a path pointing to a file
        isFile = os.path.isfile(path)

        if isFile == False:
            df = pd.DataFrame({'Product Name': products, 'Prices': prices, 'Ratings': ratings})
            df.head()
            df.to_csv(file_name, mode='a', index=False)
        else:
            df = pd.DataFrame({'Product Name': products, 'Prices': prices, 'Ratings': ratings})
            df.to_csv(file_name, mode='a', index=False, header=False)


    w0 = Label(root, text='', font=('Times', 12))
    w0.pack()
    w1 = Label(root, text='Flikart Scraper',font=('Times', 24))
    w1.pack()
    w9 = Label(root, text='', font=('Times', 12))
    w9.pack()
    w2 = Label(root, text='File created!!',font=('Times', 18))
    w2.pack()

    root.mainloop()


def get_file():
    root = Tk()
    root.title("Web Scraper")
    root.geometry("800x370")

    img = image.resize((180, 70))

    my_img = ImageTk.PhotoImage(img)

    w9 = Label(root, text='', font=('Times', 6))
    w9.pack()
    label = Label(root, image=my_img)
    label.pack()

    def filename():
        global file_name
        file_name = entry1.get()
        root.destroy()
        scrape()

    w = Label(root, text='', font=('Times', 6))
    w.pack()
    w1 = Label(root, text='Flikart Scraper',font=('Times', 24))
    w1.pack()
    w0 = Label(root, text='', font=('Times', 12))
    w0.pack()
    w2 = Label(root, text='Enter the File Name',font=('Times', 18))
    w2.pack()
    w3 = Label(root, text='{Enter file name as filenme.csv}',font=('Times', 14))
    w3.pack()
    global entry1
    entry1 = Entry(root, width=100)
    entry1.focus_set()
    entry1.pack()

    ttk.Button(root, text="Enter", width=20, command=filename).pack(pady=20)
    root.mainloop()


root = Tk()
root.title("Web Scraper")
root.geometry("800x370")
image=Image.open('flipkartimg.jpg')

img=image.resize((180, 70))

my_img=ImageTk.PhotoImage(img)

w9 = Label(root, text='', font=('Times', 6))
w9.pack()
label=Label(root, image=my_img)
label.pack()

def linkl():
    global link_n
    link_n = entry2.get()
    print(link_n)
    root.destroy()
    get_file()

w = Label(root, text='',font=('Times', 6))
w.pack()
w1 = Label(root, text='Flikart Scraper',font=('Times', 24))
w1.pack()
w0 = Label(root, text='',font=('Times', 12))
w0.pack()
w2 = Label(root, text='Enter link',font=('Times', 18))
w2.pack()
global entry2
entry2 = Entry(root, width=100)
entry2.focus_set()
entry2.pack()

ttk.Button(root, text="Enter", width=20, command=linkl).pack(pady=20)
root.mainloop()




