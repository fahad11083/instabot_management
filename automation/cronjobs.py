from automation.models import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import codecs, os, time, datetime

def automate_like_service():
    orders = Order.objects.filter(completed=False)
    order_iterator = iter(orders)
    while True:
        order = next(order_iterator)
        if order.like_service_purchased: like_service(order.amount_of_likes, order.picture_link)
        elif order.comment_service_purchased: comment_service(order.number_of_users, order.picture_link, order.comment_message)
        elif order.follower_service_purchased: follower_service(order.number_of_followers, order.account_link)
        else: print("NO SERVICE PURCHASED")
        order.completed = True
        order.save()


def like_service(amount_of_likes, url):
    credentials = Account.objects.all()[:amount_of_likes]
    for credential in credentials:
        driver = sign_in(credential)
        like_image(driver, url, credential.id)
        driver.close()


def comment_service(number_of_comments, picture_link, comment_message):
    credentials = Account.objects.all()[:number_of_comments]
    for credential in credentials:
        driver = sign_in(credential)
        comment_picture(driver, picture_link, comment_message, credential.id)
        driver.close()


def follower_service(number_of_followers, account_link):
    credentials = Account.objects.all()[:number_of_followers]
    for credential in credentials:
        try:
            driver = sign_in(credential)
            follow_user(driver, account_link, credential.id)
            driver.close()
        except Exception as e:
            print(e)


def sign_in(credential):
    PROXY = "5.79.66.2:13010"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 11; SM-A202F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)
    driver.find_element_by_name("username").send_keys(credential.email)
    driver.find_element_by_name("password").send_keys(credential.password)
    driver.find_element_by_xpath("//div[contains(text(), 'Log In')]").click()
    time.sleep(10)
    driver.save_screenshot(f"screenshot-{credential.id}-{datetime.datetime.now()}.png")
    try:
        saved_info = driver.find_element_by_xpath("//button[contains(text(), 'Not')]")
        if saved_info: saved_info.click()
    except:
        pageSource = driver.page_source
        print(pageSource)
        n = os.path.join("/home/ubuntu/apps/instabot_management",f"page_not-{credential.id}.html")
        file = codecs.open(n, "w", "utf−8")
        h = driver.page_source
        file.write(h)
        print("No selector Found //button[contains(text(), 'Not')]")
    time.sleep(7)
    try:
        add_home_screen = driver.find_element_by_xpath("//button[contains(text(), 'Cancel')]")
        if add_home_screen: add_home_screen.click()
    except:
        pageSource = driver.page_source
        print(pageSource)
        n = os.path.join("/home/ubuntu/apps/instabot_management/screenshots",f"page_cancel-{credential.id}.html")
        file = codecs.open(n, "w", "utf−8")
        h = driver.page_source
        file.write(h)
        print("No selector Found //button[contains(text(), 'Cancel')]")
    time.sleep(5)
    driver.save_screenshot(f"screenshot-{credential.id}-{datetime.datetime.now()}.png")
    return driver


def like_image(driver, url="https://www.instagram.com/p/CSTcI7gIoN2/", account_id=None):
    driver.get(url)
    time.sleep(5)
    driver.save_screenshot(f"screenshot-{account_id}-{datetime.datetime.now()}.png")
    driver.find_element_by_xpath("//button[@type='button']//span//*[name()='svg' and @aria-label='Like' and @height='24']").click()
    time.sleep(5)
    driver.save_screenshot(f"screenshot-{account_id}-{datetime.datetime.now()}.png")
    driver.close()


def follow_user(driver, url, account_id=None):
    try:
        driver.get(url)
        time.sleep(5)
        follow_button = driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
        driver.save_screenshot(f"screenshots/screenshot-{account_id}-{datetime.datetime.now()}.png")
        follow_button.click()
        time.sleep(5)
        driver.save_screenshot(f"screenshots/screenshot-{account_id}-{datetime.datetime.now()}.png")
        print("successfully Followed")
        driver.close()
    except Exception as e:
        save_page(driver, account_id, e)


def comment_picture(driver, url, message, account_id=None):
    driver.get(url)
    time.sleep(5)
    driver.save_screenshot(f"screenshots/screenshot-{account_id}-{datetime.datetime.now()}.png")
    driver.find_element_by_xpath("//button[@type='button']//div//*[name()='svg' and @aria-label='Comment' and @height='24']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//textarea[contains(@aria-label, 'Add a comment')]").send_keys(message)
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(text(), 'Post')]").click()
    time.sleep(5)
    driver.save_screenshot(f"screenshots/screenshot-{account_id}-{datetime.datetime.now()}.png")
    driver.close()


def save_page(driver, id, e):
    pageSource = driver.page_source
    print(pageSource)
    n = os.path.join("/home/ubuntu/apps/instabot_management/screenshots", f"page_{e}-{id}.html")
    file = codecs.open(n, "w", "utf−8")
    h = driver.page_source
    file.write(h)