from selenium import webdriver

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.binary_location = '/usr/bin/google-chrome'
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    capabilities = options.to_capabilities()

    driver = webdriver.Remote(command_executor='http://chromedriver:9515', desired_capabilities=capabilities)
    try:
        driver.get('https://qiita.com/advent-calendar/2017/docker')
        print('title:', driver.title)
        print('text:', driver.find_element_by_css_selector('article').text)
    finally:
        driver.quit()
