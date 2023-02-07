import requests
from bs4 import BeautifulSoup

f = open('dineout_data.txt', 'w')
f.write('Hotel details\n')
f.write('Website : https://www.dineout.co.in/\n')
f.write('City : Indore\n')
f.write('State : Madhya Pradesh\n')
f.write('\n______________________________________________________________\n\n')

## Step 1: Get HTML
Restaurant_no = 0
for page_no in range(61):
    url = 'https://www.dineout.co.in/indore-restaurants?search_str=indore&p='
    url = url+str(page_no)
    r = requests.get(url)
    htmlcontent = r.content
    print('Page number : {}\n'.format(page_no))
    f.write('Page number : {}\n'.format(page_no))

    ## Step 2: Parse the HTML
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    detail = soup.find_all('div', class_='restnt-info cursor')
    for details in detail:
        Restaurant_no += 1
        print('Restaurant no. : {}\n'.format(Restaurant_no))
        f.write('Restaurant no. : {}\n'.format(Restaurant_no))
        rest_name = details.find('a', href=True).text
        print('Restaurant name : {}\n'.format(rest_name))
        f.write('Restaurant name : {}\n'.format(rest_name))
        rest_url = 'https://www.dineout.co.in/'+details.find('a', href=True)['href']
        print('Website : {}\n'.format(rest_url))
        f.write('Website : {}\n'.format(rest_url))
        location = details.find('div',class_='restnt-loc ellipsis').text
        print('Location : {}\n'.format(location))
        f.write('Location : {}\n'.format(location))
        r1 = requests.get(rest_url)
        htmlcontent1 = r1.content

        ## Step 2: Parse the HTML
        try:
            soup1 = BeautifulSoup(htmlcontent1, 'html.parser')
            lnk = soup1.find_all('a', class_ = 'body-color')
            print('Phone number : {}\n'.format(lnk[2].get('href')))
            f.write('Phone number : {}\n'.format(lnk[2].get('href')))
        except:
            print('No phone number')
            f.write('No phone number')
        print('\n_________________________________________________________________\n\n')
        f.write('\n_________________________________________________________________\n\n')