from datetime import datetime
from selenium import webdriver

class FlightInfo:
    def __init__(self, origin, destination, month):
        self.origin = origin
        self.destination = destination
        self.month = month
        self.date = None
        self.price = None
        self.today = datetime.today().day

    def skyscanner_flight_keyword_search(self):
        driver = webdriver.Chrome('/Users/Chrisaor/projects/hackerthon/fc_hackerthon_wps_team5/chromedriver')
        driver.implicitly_wait(3)
        url = 'http://www.skyscanner.co.kr/transport/flights/'
        url += f'{self.origin}/'
        url += f'{self.destination}/'
        url += f'?oym=180{self.month}'
        url += f'&selectedoday={self.today}'
        url += f'&rtn=0'

        driver.get(url)

        tds = driver.find_elements_by_class_name('bpk-calendar-grid__date-3CZvx')

        day_list = list()
        price_list = list()
        for td in tds:
            days = td.find_elements_by_class_name('date')
            prices = td.find_elements_by_class_name('price')
            for day in days:
                day_list.append(day.text)
            for price in prices:
                price_list.append(price.text)

        # day_price_dict = dict(zip(day_list, price_list))

        result = list()
        for i in range(len(day_list)):
            self.date = day_list[i]
            self.price = price_list[i]
            price_info = PriceInfo(self.date, self.price)
            result.append(price_info)

        return result


class PriceInfo:
    def __init__(self, date, price):
        self.date = date
        self.price = price

    def __repr__(self):
        return f'{self.date}일의 가격: {self.price}'

    def __str__(self):
        return f'{self.date}일의 가격: {self.price}'



# seoul_to_osaka_7 = FlightInfo('sela', 'osaa', 7)
# # seoul_to_osaka_8 = FlightTicket('sela', 'osaa', 8)
# seoul_to_osaka_7.skyscanner_flight_keyword_search()
# seoul_to_osaka_8.skyscanner_flight_keyword_search()

