from bs4 import BeautifulSoup
import urllib.request
import requests
import time

def read_website(url, addon = ""):
    response = requests.get(url + addon)
    time.sleep(7)
    soup = BeautifulSoup(response.text,'html.parser')
    return(soup)
    

def scrape_weather(file_name):    
    
    base_url = 'https://www.almanac.com/weather/history/ON/Toronto/'
    year = [str(x) for x in list(range(1969,2019))]
    month = ['03','04','05','06','07','08','09','10']
    day_per_month = {'03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30,'10': 31}


    file = open(file_name,'w')
    file.write('Date, Temperature, Precipitation \n')

    for cur_year in year:
        for cur_month in month:
            for day in range(1,day_per_month[cur_month]+1):
                cur_date = (str(cur_year) + '-' + str(cur_month) + '-' + str(day))
                soup = read_website(base_url,cur_date)                         
                file.write(str(cur_date) + ',' + str(soup.find(class_ = "weatherhistory_results_datavalue temp").get_text()) + ',' + str(soup.find(class_ = "weatherhistory_results_datavalue prcp").get_text()) + '\n')
                print(cur_date)
    file.close()


def baseball_scrapper():
    
    baseball_links = ['https://www.retrosheet.org/gamelogs/gl1970_79.zip',
                  'https://www.retrosheet.org/gamelogs/gl1980_89.zip',
                  'https://www.retrosheet.org/gamelogs/gl1990_99.zip',
                  'https://www.retrosheet.org/gamelogs/gl2000_09.zip',
                  'https://www.retrosheet.org/gamelogs/gl2010_19.zip']
    
    for link in baseball_links:
        name = link.split('/')[-1]
        urllib.request.urlretrieve(link, name)
        print(name + ' is done')
        

if __name__ == '__main__':

    baseball_scrapper()
    scrape_weather('TorontoWeather.txt')