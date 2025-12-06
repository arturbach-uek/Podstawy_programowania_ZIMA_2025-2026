import csv

def copy_genre(genre, filename):
    with open('books.csv') as f:
        reader = csv.DictReader(f)
        with open(filename, 'w') as out:
            for row in reader:
                if row['Genre'] == genre:
                    out.write(','.join(row.values())+'\n')

copy_genre('Fantasy', 'books_fantasy.txt')
copy_genre('Historical', 'books_historical.txt')
copy_genre('Romance', 'books_romance.txt')
copy_genre('Classic', 'books_classic.txt')
