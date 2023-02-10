import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


s = Service("C:/Users/shree/Desktop/chromedriver.exe") #webdriver path

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

#open webbrowser
driver = webdriver.Chrome(service = s, options = options)
#search the link
driver.get('https://agmarknet.gov.in/')
time.sleep(2)

#click on "Price Trend"
price_trend = driver.find_element(by = By.XPATH, value = '//*[@id="menu"]/ul/li[4]/a')
price_trend.click()
time.sleep(2)

#click on "market wise report"
market_wise_report = driver.find_element(by = By.XPATH, value = '//*[@id="cphBody_Accordion1"]/div[5]')
market_wise_report.click()
time.sleep(2)

#click on "market wise wholesale prices weekly analysis"
market_wise_wholsale_price_weekly_analysis = driver.find_element(by = By.XPATH, value = '//*[@id="cphBody_Accordion1"]/div[6]/div/div/ul/li[5]/a')
market_wise_wholsale_price_weekly_analysis.click()


months = ['November', 'December'] #list of months
weeks = ['First', 'Second', 'Third', 'Fourth'] #list of week

for m in months:
    for w in weeks:

        # Select "Commodity"
        try:
            commodity_dropdown = driver.find_element(by = By.XPATH, value = '//td[.= "Commodity"]/parent::tr//select')
            commodity = Select(commodity_dropdown)
            commodity.select_by_visible_text("Groundnut") #commodity
            time.sleep(10)
        except:
            print("Enter valid commodity")

        #Select "State"
        try:
            state_dropdown = driver.find_element(by = By.XPATH, value = '//td[.= "State"]/parent::tr//select')
            state = Select(state_dropdown)
            time.sleep(3)
            state.select_by_visible_text("Gujarat") #state
            time.sleep(10)
        except:
            print("Enter Valid State")


        #Select "District"
        try:
            district_dropdown = driver.find_element(by = By.XPATH, value = '//td[.= "District"]/parent::tr//select')
            district = Select(district_dropdown)
            time.sleep(3)
            district.select_by_visible_text("Amreli") #district
            time.sleep(10)
        except:
            print('Enter Valid District')

        #Select "Year"
        try:
            year_dropdown = driver.find_element(by = By.XPATH, value = '//td[.= "Year"]/parent::tr//select')
            year = Select(year_dropdown)
            time.sleep(3)
            year.select_by_visible_text("2022") #year
            time.sleep(10)
        except:
            print("Year not found")



        #Select "Month"

        month_dropdown = driver.find_element(by = By.XPATH, value = '//td[.= "Month"]/parent::tr//select')
        month = Select(month_dropdown)
        time.sleep(3)
        month.select_by_visible_text(m) #month
        time.sleep(10)


        #Select "Week"
        try:
            week_dropdown = driver.find_element(by = By.XPATH, value = '//td[.= "Week"]/parent::tr//select')
            week = Select(week_dropdown)
            time.sleep(3)
            week.select_by_visible_text(w) #week
            time.sleep(10)
        except:
            print("Enter Correct Week Number")
            driver.get('https://agmarknet.gov.in/PriceTrends/SA_Week_PriM.aspx')#If week number is not in a list then go back and take a next week number
            time.sleep(2)
            continue


        #Click on "Submitt"
        submitt = driver.find_element(by = By.XPATH, value = '//*[@id="cphBody_But_Submit"]')
        submitt.click()
        time.sleep(2)

        #Click on "Export / download excel file"
        export = driver.find_element(by = By.XPATH, value = '//*[@id="cphBody_Button1"]')
        export.click()

        driver.get('https://agmarknet.gov.in/PriceTrends/SA_Week_PriM.aspx')
        time.sleep(10)