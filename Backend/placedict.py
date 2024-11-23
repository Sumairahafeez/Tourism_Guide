import csv
import sortingAlgorithms
csv_file = 'Places.csv'
def ReadCsv():
    places = []
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
                places.append({
                    'name': row[0],
                    'ratings': row[1],
                    'category': row[2]
                })
                print("places loaded successfully")    
    except FileNotFoundError:
        print('File not found')  
def writeCsv(places):
    try:
        with open(file=csv_file, mode = 'w') as file:
            writer = csv.writer(file)
            writer.writeheader(['Name', 'Ratings', 'Category'])
            writer.writerows(places) 
            print('places written successfully')
    except FileNotFoundError:
        print('File not found')                         
def AddPlace(name,ratings,category):
    places = ReadCsv()
    if any(places['name'].lower() == name.lower() for place in places):
        print('Place already exists')
    else:
        places.append({
            'name': name,
            'ratings': ratings,
            'category': category
        })
        writeCsv(places)
def GetTop6Places():
    places = ReadCsv()
    Ratings = [places['ratings'] for rating in places]  
    sortingAlgorithms.bubbleSort(Ratings)
    top6 = Ratings[:6]
    return [place for place in places if place['ratings'] in top6]