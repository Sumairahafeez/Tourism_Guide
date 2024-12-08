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
                    'Name': row[0],
                    'Ratings': row[1],
                    'Category': row[2],
                })
                print("places loaded successfully")        
    except FileNotFoundError:
        print('File not found')  
    return places    
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
    if any(places['Name'].lower() == name.lower() for place in places):
        print('Place already exists')
    else:
        places.append({
            'Name': name,
            'Ratings': ratings,
            'Category': category
        })
        writeCsv(places)
def GetTop6Places():
    places = ReadCsv()
    Ratings = [place['Ratings'] for place in places]  
    sortingAlgorithms.bubbleSort(Ratings)
    top6 = Ratings[:6]
    return [place for place in places if place['Ratings'] in top6]
def GetRandomPlaces():
    places = ReadCsv()
    RandomPlaces = [place['Ratings'] for place in places]
    sortingAlgorithms.shuffleArray(RandomPlaces)
    return [place for place in places if place['Ratings'] in RandomPlaces[:6]]
def GetPlacesByCategory(category):
    places = ReadCsv()
    return [place for place in places if place['Category'].lower == category.lower()] 
