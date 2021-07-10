from selenium import webdriver


hs_inven_url = "https://www.inven.co.kr/board/hs/3508?come_idx=3508&category=유저"
driver = None


def get_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # 웹 브라우저를 띄우지 않는 headless chrome 옵션 적용
    options.add_argument('disable-gpu')  # GPU 사용 안함
    options.add_argument('lang=ko_KR')  # 언어 설정
    return webdriver.Chrome('chromedriver', options=options)  # 옵션 적용


def get_article_list():
    global driver
    if driver is None:
        driver = get_chrome_driver()
    driver.get(hs_inven_url)
    return driver.find_elements_by_xpath("//tr[contains(@class, 'ls') and contains(@class, 'oh') and contains(@class, 'tr')]")


def get_class(obj, name):
    return obj.find_element_by_class_name(name)


def get_name_of_class(obj, name):
    return get_class(obj, name).text
