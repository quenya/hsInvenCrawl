import selenium_util as su
import file_io as fi
import time
import datetime


interval_time = 10 * 60


def update_last_num(new_article_list):
    last_num = new_article_list[-1][0]
    print('last_number: %d' % last_num)
    fi.write_last_num(last_num)


def notify_new_article_list(new_article_list, now):
    print('[%s] %d articles added' % (now, len(new_article_list)))
    for num, title, href in new_article_list[::-1]:
        print('%d - %s: %s' % (num, title, href))


def get_new_article_list():
    article_list = su.get_article_list()
    last_num = fi.read_last_num()
    new_article_list = []
    for article in article_list:
        num = int(su.get_name_of_class(article, 'bbsNo'))
        if num <= last_num:
            break
        doc = su.get_class(article, 'sj_ln')
        title = doc.text
        href = doc.get_property('href')
        new_article_list.append((num, title, href))
    return new_article_list


def main_crawl_logic():
    new_article_list = get_new_article_list()
    now = datetime.datetime.now()
    if len(new_article_list) is 0:
        print('[%s] no added article' % now)
        return
    notify_new_article_list(new_article_list, now)
    update_last_num(new_article_list)


if __name__ == '__main__':
    while True:
        main_crawl_logic()
        time.sleep(interval_time)