from selenium import webdriver


def get_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # 웹 브라우저를 띄우지 않는 headless chrome 옵션 적용
    options.add_argument('disable-gpu')  # GPU 사용 안함
    options.add_argument('lang=ko_KR')  # 언어 설정
    return webdriver.Chrome('chromedriver', options=options)  # 옵션 적용


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver = get_chrome_driver()
    hs_inven_url = "https://www.inven.co.kr/board/hs/3508?come_idx=3508&category=유저"
    driver.get(hs_inven_url)
    doc_list = driver.find_elements_by_xpath("//tr[contains(@class, 'ls') and contains(@class, 'oh') and contains(@class, 'tr')]")
    print(doc_list)
    for doc in doc_list:
        num = doc.find_element_by_class_name('bbsNo').text
        article = doc.find_element_by_class_name('sj_ln')
        title = article.text
        href = article.get_property('href')
        print('%s - %s: %s' % (num, title, href))
