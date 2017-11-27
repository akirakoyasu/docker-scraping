from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

if __name__ == '__main__':
    driver = webdriver.Remote(command_executor='http://selenium:4444/wd/hub',
                              desired_capabilities=DesiredCapabilities.CHROME.copy())
    try:
        driver.get('https://qiita.com/advent-calendar/2017/docker')
        print('title:', driver.title)
        print('text:', driver.find_element_by_css_selector('article').text)
    finally:
        driver.quit()
