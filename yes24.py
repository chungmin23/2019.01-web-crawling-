from selenium import webdriver
from selenium.webdriver.common.keys import Keys # enter를 입력하기 위한것
#from selenium.webdriver.common.action_chains import ActionChains
from myid import ID, PW # id pw 지정
import pyautogui
import time # time패키지

#driver = webdriver.PhantomJS('C:/Program Files/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)

try:
    driver.get('http://starcandy.yes24.com/Save/AttendBook.aspx')

    elem = driver.find_element_by_link_text('로그인') #링크안에 텍스트 값을 추출 할때
    elem.click() # 클릭하기

    time.sleep(1) # 이 시간동안 기다린다 . 페이지만 바뀌게 되어서 미리 아이디 비밀번호를 바뀐다
    # 로그인 하기
    elem = driver.find_element_by_name('SMemberID')
    elem.send_keys(ID)
    elem = driver.find_element_by_name('SMemberPassword')
    elem.send_keys(PW)
    elem.send_keys(Keys.RETURN) # enter 클릭

    time.sleep(2)
   
    elem2 = driver.find_element_by_css_selector("input[name*='PollNum']").click()
    elem= driver.find_element_by_xpath(".//option[@value='1']").click()
    elem = driver.find_element_by_xpath(".//div[@class='todaywrite']/a").click()
    pyautogui.press('enter')
    time.sleep(1)

    elem = driver.find_element_by_xpath(".//div[@id='AttendGB']/div[3]/a").click()
    pyautogui.press('enter')
    #elem.send_keys(Keys.ENTER)
    input()
except Exception as e:
    print(e)
finally:
    driver.quit()