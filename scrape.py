import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def main():

    r = requests.get("http://www.nfl.com/players/search?category=position&filter=quarterback&conferenceAbbr=null&playerType=current&conference=ALL")

    while True:
        
        soup = BeautifulSoup(r.text, "html.parser")
        
        players = soup.find(id = 'result').find("tbody").find_all("tr") 
        
        for player in players:
            if player.find_all("td")[3].get_text() != 'CUT' or 'DEV':
                print name_reverse(player.find_all("td")[2].get_text())
        
    
        if len(soup.find_all('a',text = 'next')) > 0:
            
            r = requests.get("http://www.nfl.com"+soup.find_all('a',text = 'next')[0].get('href'))
        else:
            break
        print "-----------------------------------"
        


def name_reverse(name):
    name = name.split(',')
    name[0],name[1] = name[1],name[0]
    return ' '.join(map(str,name))


main()