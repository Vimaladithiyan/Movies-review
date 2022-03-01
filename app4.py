from tkinter import *
import tkinter as tk
from tkinter import ttk



root = Tk()



root.geometry("400x250")
movies = []
START = "\nEnter 'a' to add a movie, \n 'l' to see your movies, \n 'f' to find a movie by title,\n 'r' to find ratings, \n or 'q' to quit: "
t=tk.StringVar()
y=tk.StringVar()
d=tk.StringVar()
g=tk.StringVar()





def inputmov():

  title = Label(root, font=('calibre',10,'normal'), text = "Title").place(x = 30,y = 50)
  year = Label(root, font=('calibre',10,'normal'), text = "Year").place(x = 30, y = 90)
  director = Label(root, font=('calibre',10,'normal'),text = "Director").place(x = 30, y = 130)
  genre = Label(root, font=('calibre',10,'normal'),text = "Genre").place(x = 30, y = 170)
  e1 = Entry(root,textvariable = t, font=('calibre',10,'normal')).place(x = 80, y = 50)
  e2 = Entry(root,textvariable = y, font=('calibre',10,'normal')).place(x = 80, y = 90)
  e3 = Entry(root,textvariable = d, font=('calibre',10,'normal')).place(x = 95, y = 130)
  e4 = Entry(root,textvariable = g, font=('calibre',10,'normal')).place(x = 100, y = 170)
  ttk.Button(root, text='Submit', command=lambda: add_movie()).pack()

#name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
#sub_btn=tk.Button(root,text = 'Submit', command = submit)


def add_movie():
  title=t.get() 
  year=y.get()
  director=d.get()
  genre=g.get()



  y.set("")
  t.set("")
  d.set("")
  g.set("")
  
  movies.append({
  'title': title,
  'year': year,
  'director': director,
  'genre': genre,
  })



def list_movies():
   quantity = len(movies)
   titles = [movie['title'] for movie in movies]
   titles = ', '.join(titles)



   if quantity:
       print(f'You have following movies in collection: {titles}. In total you have {quantity} {"movie" if quantity == 1 else "movies"}.')
   else:
       print('There are no movies in you collection.')



    

def print_movie_info(movie):
   print('Here is information about requested title')
   print(f'Title: {movie["title"]},')
   print(f'Director: {movie["director"]},')
   print(f'Year: {movie["year"]},')
   print(f'Genre: {movie["genre"]}.')




def find_title():
     search_title = input('Enter title you are looking for: ')
     for movie in movies:
         if movie['title'] == search_title:
            print_movie_info(movie)
         else:
            print('Requested title was not found in the collection.')








ttk.Button(root, text='add movie', command=lambda: inputmov()).pack()
ttk.Button(root, text='list movie',command=lambda: list_movies()).pack()
ttk.Button(root, text='movie info', command=lambda: print_movie_info(movie)).pack()
root.mainloop()

