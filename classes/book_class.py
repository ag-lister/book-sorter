"""
* Name        : book_class.py
* Author      : Andy Lister
* Created     : 12/17/2020
* Course      : CIS 152 Data Structures
* Version     : 1.0
* OS          : Windows 10
* Copyright   : This is my own original work based on
*               specifications issued by our instructor
* Description : This file holds the Book class used by my final_gui.py
*               Input:  none
*               Output: none
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to
* my program.
"""


class Book:
    """Book class"""
    # constructor
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        if genre == "\n":
            self.genre = "n/a" + "\n"
        else:
            self.genre = genre
