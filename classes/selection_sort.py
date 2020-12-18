"""
* Name        : selection_sort.py
* Author      : Andy Lister
* Created     : 12/17/2020
* Course      : CIS 152 Data Structures
* Version     : 1.0
* OS          : Windows 10
* Copyright   : This is my own original work based on
*               specifications issued by our instructor
* Description : This file holds the selection sort used by my final_gui.py
*               Input:  none
*               Output: none
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access to
* my program.
"""


def selection_sort(book_array, sorting):
    """
    This function takes in the array of books and a string sorting to do a selection
    sort on the array.
    :param book_array: array of Book
    :param sorting: string
    :return:
    """
    if sorting == "author":
        for i in range(len(book_array)):
            min_index = i

            for b in range(i + 1, len(book_array)):
                author1 = str(book_array[min_index].author)
                author2 = str(book_array[b].author)
                author1 = author1.split(" ")
                author2 = author2.split(" ")
                if author1[len(author1) - 1] > author2[len(author2) - 1]:
                    min_index = b

            book_array[i], book_array[min_index] = book_array[min_index], book_array[i]

    elif sorting == "title":
        for i in range(len(book_array)):
            min_index = i

            for b in range(i + 1, len(book_array)):
                title1 = str(book_array[min_index].title)
                title2 = str(book_array[b].title)
                title1 = title1.split(" ")
                title2 = title2.split(" ")
                if title1[0] == "The" and title2[0] == "The":
                    if str(title1[1]) > str(title2[1]):
                        min_index = b
                elif title1[0] == "The" and title2[0] != "The":
                    if str(title1[1]) > str(book_array[b].title):
                        min_index = b
                elif title1[0] != "The" and title2[0] == "The":
                    if str(book_array[min_index].title) > str(title2[1]):
                        min_index = b
                elif str(book_array[min_index].title) > str(book_array[b].title):
                    min_index = b

            book_array[i], book_array[min_index] = book_array[min_index], book_array[i]
