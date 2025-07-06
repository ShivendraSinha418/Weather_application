from django.shortcuts import render
import requests 
from bs4 import BeautifulSoup

def scrap_current(city):
    web = requests.get(f"https://www.theweathernetwork.com/en/city/in/uttar-pradesh/{city}/current")
    if(web.status_code == 200):
        soup = BeautifulSoup(web.content,'html.parser')
        temp = soup.find_all('div',class_="sc-IqJVf hDXsVu")
        weather_statement = soup.find_all('div',class_="sc-eiQriw bzLxpG")
        feels_like = soup.find_all('div',class_='sc-fPXMVe iePLDC')
        check = soup.find_all('div',class_='sc-ffZAAA bQbGXB')
        image = check[0].find('img')
        hourly_status = soup.find_all('div',class_='sc-fPXMVe bOMCOg')
        hourly_status_temp = soup.find_all('div',class_='sc-fPXMVe kelCDF')
        hourly_status_feels = soup.find_all('div',class_='sc-fPXMVe hWjImN')
        return temp[0].text , image.get('src') , weather_statement[0].text , feels_like[0].text , feels_like[1].text,hourly_status,hourly_status_temp,hourly_status_feels
    else :
        print('Weather data cannot be fetched please try after some time')
def index(request):
    city =""
    if request.method == "POST":
        city = request.POST.get('city')
    if city =="":
        city = 'delhi'
    weather_details = scrap_current(city)
    if(weather_details!= None):
        Context ={
        'temperature': weather_details[0],
        'weather_img': weather_details[1],
        'weather_status': weather_details[2],
        'Feels' : weather_details[3],
        'HnL' : weather_details[4],
        'time_1': weather_details[5][0].text,  
        'time_2': weather_details[5][1].text,
        'time_3': weather_details[5][2].text,
        'time_4': weather_details[5][3].text,
        'time_5': weather_details[5][4].text,
        'temp_1': weather_details[6][0].text,  
        'temp_2': weather_details[6][1].text,
        'temp_3': weather_details[6][2].text,
        'temp_4': weather_details[6][3].text,
        'temp_5': weather_details[6][4].text,
        'feels_1': weather_details[7][0].text,  
        'feels_2': weather_details[7][1].text,
        'feels_3': weather_details[7][2].text,
        'feels_4': weather_details[7][3].text,
        'feels_5': weather_details[7][4].text
        }
    else :
        Context ={
        'temperature': '',
        'weather_img': '',
        'weather_status': '',
        'Feels' : '',
        }
    return render(request,'index.html',Context)
