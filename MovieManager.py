#http://www.omdbapi.com/?t=batman&apikey=aabca0d
import urllib.parse,urllib.error,urllib.request
import json
import tkinter

def movieFetcher(data):
    Title = data['Title']
    Year = data['Year']
    Released_Date = data['Released']
    Director = data['Director']
    Language = data['Language']
    Plot = data['Plot']
    Awards = data['Awards']
    Imdb = data['Ratings'][0]['Value']
    Imdb_votes = data['imdbVotes']
    Rotten_Tomato = data['Ratings'][1]['Value']
    print('Title: ', Title)
    print('Year:  ', Year)


serviceurl = "http://www.omdbapi.com/?"
top = tkinter.Tk()
L1 = tkinter.Label(top,text = 'Movie name ')
L1.pack( side = 'left')
E1 = tkinter.Entry(top, bd =5)
E1.pack(side = 'right')
top.mainloop()

#movie_name = input('Enter Name Of The Movie: ')
url = serviceurl + urllib.parse.urlencode({'t':movie_name})
url += '&apikey=aabca0d'
print('Retrieving From: ',url)
hn = urllib.request.urlopen(url).read().decode()
#print('Response: ',hn)
data = json.loads(hn)
movieFetcher(data)



