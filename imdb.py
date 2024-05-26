import csv
import tkinter as tk
from tkinter import messagebox

# Fonction pour charger l'ensemble de données à partir d'un fichier CSV
def load_dataset(file_name):
    dataset = []
    with open(file_name, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            dataset.append(row)
    return dataset

# Fonction pour afficher tous les films et leurs évaluations dans une liste
def view_all_movies(dataset):
    
    # Crée une nouvelle fenêtre
    window = tk.Tk()
    window.title("Netflix Movie Rating System")

    # Crée une liste pour afficher les films et leurs évaluations
    listbox = tk.Listbox(window, width=50, height=20)
    listbox.pack(padx=10, pady=10)

    # Ajoute chaque film et son évaluation à la liste
    for movie in dataset:
        listbox.insert(tk.END, f"{movie[0]} - Rating: {movie[1]}")

    # Fonction pour gérer le clic sur le bouton de recherche
    def search_movie():
        search_term = entry_search.get().lower()
        search_result = []
        for movie in dataset:
            if search_term in movie[0].lower():
                search_result.append(f"{movie[0]} - Rating: {movie[1]}")
        if search_result:
            messagebox.showinfo("Search Result", '\n'.join(search_result))
        else:
            messagebox.showinfo("Search Result", "No movies found matching the search term.")

    # Fonction pour gérer le clic sur le bouton d'ajout
    def add_movie():
        title = entry_title.get().strip()
        rating = entry_rating.get().strip()
        if title and rating:
            dataset.append([title, rating])
            listbox.insert(tk.END, f"{title} - Rating: {rating}")
            messagebox.showinfo("Success", "Movie added successfully.")
        else:
            messagebox.showwarning("Warning", "Please enter both movie title and rating.")

    # Champs d'entrée et boutons pour la recherche et l'ajout de films
    tk.Label(window, text="Search Movie:").pack()
    entry_search = tk.Entry(window, width=30)
    entry_search.pack()
    btn_search = tk.Button(window, text="Search", command=search_movie)
    btn_search.pack()

    tk.Label(window, text="Add Movie Title:").pack()
    entry_title = tk.Entry(window, width=30)
    entry_title.pack()
    tk.Label(window, text="Add Movie Rating:").pack()
    entry_rating = tk.Entry(window, width=30)
    entry_rating.pack()
    btn_add = tk.Button(window, text="Add Movie", command=add_movie)
    btn_add.pack()

    # Bouton pour quitter l'application
    btn_exit = tk.Button(window, text="Exit", command=window.quit)
    btn_exit.pack()

    window.mainloop()

# Fonction principale
def main():
    dataset = load_dataset(r"C:\\Users\\PL\\Desktop\\MINI PROJET ML\\imdb_data1.csv")
    view_all_movies(dataset)

if __name__ == "__main__":
    main()
