"""
* Name        : final_gui.py
* Author      : Andy Lister
* Created     : 12/17/2020
* Course      : CIS 152 Data Structures
* Version     : 1.0
* OS          : Windows 10
* Copyright   : This is my own original work based on
*               specifications issued by our instructor
* Description : This is the book organizing GUI I made for my final for data structures. It includes
*               the use of a queue and array to read in books from a file and add new books to it.
*               Input:  Book title and author required, genre optional
*               Output: A list of books organized by title or author, user's choice
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to
* my program.
"""
import os as os
from tkinter import *
from classes.book_class import Book
from classes.selection_sort import selection_sort
from tkinter import messagebox

#  declared globally for ease of use
book_queue = []
array = []  # (data structure 1)


def add_book():
    """
    This function handles input validation for the form fields as well as the creation
    of the Book object and its insertion into the queue when the add book button is pressed.
    :return:
    """
    entered_title = title_field.get()
    entered_author = author_field.get()
    entered_genre = genre_field.get()

    # input validation
    if entered_title == "" or entered_author == "":
        messagebox.showinfo("", "Author and title fields cannot be left blank")
        return

    accepted_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' -0123456789")
    if not (accepted_characters.issuperset(entered_title) and accepted_characters.issuperset(entered_author)):
        messagebox.showinfo("", "Please make sure title and author are spelled correctly")
        return

    if entered_genre != "":
        if not (accepted_characters.issuperset(entered_genre)):
            messagebox.showinfo("", "Please make sure the genre is spelled correctly")
            return
    #  Only creates book and adds to queue if it makes it this far in the function
    book_queue.append(Book(entered_title, entered_author, entered_genre + "\n"))
    messagebox.showinfo("", "Book added!")
    author_field.delete('0', END)
    genre_field.delete('0', END)
    title_field.delete('0', END)
    title_field.focus()


def clear():
    """
    This function handles the clearing of the queue, as well as the clearing of all
    text fields when the clear queue button is pressed.
    :return:
    """
    book_queue.clear()
    author_field.delete('0', END)
    genre_field.delete('0', END)
    title_field.delete('0', END)
    title_field.focus()
    messagebox.showinfo("", "Queue cleared!")


def sort_title():
    """
    This function handles the process of popping off the queue and calling the selection sort
    to sort by title when the "sort by title" button is pushed.
    :return:
    """
    # pops it off queue and puts it into array to sort (data structure #2)
    for i in range(len(book_queue)):
        array.append(book_queue.pop())

    selection_sort(array, "title")

    listbox.delete(0, END)
    for i in range(len(array)):
        listbox.insert(END, str(array[i].title) + ", " + str(array[i].author) + ", " + str(array[i].genre))


def sort_author():
    """
    This function handles the process of popping off the queue and calling the selection sort
    to sort by author when the "sort by author" button is pushed.
    :return:
    """
    # pops it off queue and puts it into array to sort (data structure #2)
    for i in range(len(book_queue)):
        array.append(book_queue.pop())

    selection_sort(array, "author")

    listbox.delete(0, END)
    for i in range(len(array)):
        listbox.insert(END, str(array[i].title) + ", " + str(array[i].author) + ", " + str(array[i].genre))


def output():
    """
    This function handles outputting the books to a text file when the output button is pressed
    :return:
    """
    try:
        with open("organized_books.txt", "w") as outfile:
            for i in range(len(array)):
                outfile.write(str(array[i].title) + "," + str(array[i].author) + "," + str(array[i].genre))
            outfile.close()
        messagebox.showinfo("", "File Created!")
    except IOError:
        print("Cannot open file on file system!")


def read_in():
    """
    This function is called on GUI launch and handles the importing of the txt file
    and creates Book objects based on what it reads in and adds them to the array
    :return:
    """
    file_dir = os.path.dirname(__file__)
    file_name = "organized_books.txt"
    f = open(os.path.join(file_dir, file_name), "r")
    for line in f.readlines():
        book = line.split(',')
        array.append(Book(book[0], book[1], book[2]))

    f.close()


#  Creates GUI
m = Tk()
m.title("Sort Books!")

#  Builds GUI
title_label = Label(m, text="Title:")
title_field = Entry(m, width=30)
title_label.grid(row=0, column=0)
title_field.grid(row=0, column=1, columnspan=2)

author_label = Label(m, text="Author:")
author_field = Entry(m, width=30)
author_label.grid(row=1, column=0)
author_field.grid(row=1, column=1, columnspan=2)

genre_label = Label(m, text="Genre:")
genre_field = Entry(m, width=30)
genre_label.grid(row=2, column=0)
genre_field.grid(row=2, column=1, columnspan=2)

#  Evens out the right side on spacing
blank_label = Label(m, text="        ")
blank_label.grid(row=0, column=4)

#  Adds listbox
listbox = Listbox(m, width=40)
listbox.grid(row=7, column=0, columnspan=5)

#  Fills listbox
read_in()
for x in range(len(array)):
    listbox.insert(END, str(array[x].title) + ", " + str(array[x].author) + ", " + str(array[x].genre))

#  Adds Buttons
button1 = Button(m, text="Add Book", command=add_book)
button1.grid(row=4, column=1)

button2 = Button(m, text="Clear All Entries", command=clear)
button2.grid(row=4, column=2)

button3 = Button(m, text="Sort All By Title", command=sort_title)
button3.grid(row=5, column=1, columnspan=2)

button4 = Button(m, text="Sort All By Author", command=sort_author)
button4.grid(row=6, column=1, columnspan=2)

button5 = Button(m, text="Output!", command=output)
button5.grid(row=8, column=1, columnspan=2)

#  Main GUI Loop
m.mainloop()
