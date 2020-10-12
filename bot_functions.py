import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from gmail_code_extracter import get_inbox



host = 'imap.gmail.com'
username = 
password = 




#logins into instagram and your account
driver =  webdriver.Chrome(ChromeDriverManager().install())
def login():
    driver.get("https://www.instagram.com/")
    time.sleep(1)
    driver.maximize_window()
    login_element = driver.find_element_by_name("username")
    login_element.send_keys("your username here")
    password_element = driver.find_element_by_name("password")
    password_element.send_keys("your password here")
    password_element.send_keys(Keys.RETURN)
    time.sleep(3)
    try:
        time.sleep(3)
        savecancel = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        savecancel.click()
        time.sleep(2)
        
    except:
        print("diffrent approach !!!")
        send_code = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/div[3]/form/span/button')
        send_code.click()
        time.sleep(30)
        my_inbox = get_inbox()
        my_inbox = my_inbox[0]
        my_inbox = str(my_inbox)
       
        pattern = re.compile(">\d\d\d\d\d\d<")
        matches = pattern.finditer(my_inbox)

        for match in matches:
            match = str(match)
            match = match[45:51]
            print(match + " !!!!!!!!!!!!!!!!!!!!!!!!!!! ")
            code_area = driver.find_element_by_xpath('//*[@id="security_code"]')
            code_area.send_keys(match)

        submit = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/div[2]/form/span/button')
        submit.click()

    cancel_button = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    cancel_button.click()

      

# follows your suggestions        
def follow_sugg():
    time.sleep(2)
    profile = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[1]/a/div')
    profile.click()
    time.sleep(1)
    num = 1
    while num <= 35:
        follow_button = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[2]/div/div/div[" + str(num) + "]/div[3]/button")
        follow_button.click()
        num += 1
        time.sleep(0)
    driver.back()   
    
        

# likes posts in an hashtag 
def like_ph_hashtag(hashtag):
# going into the hashtag itself
    search_bar = driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
    search_bar.send_keys("#" + hashtag)
    time.sleep(2)
    search_bar.send_keys(Keys.RETURN)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(3)
    pics = driver.find_elements_by_class_name('_9AhH0')
    print(hashtag + " photos " + str(len(pics)))
    print(pics)
    time.sleep(3)
# goes into each post and liking it
    first_photo = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    first_photo.click()
    next1 = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
    next1.click()
    for pic in pics :
        time.sleep(2)
        like = driver.find_element_by_class_name('fr66n')
        like.click()
        time.sleep(1)
        next2 = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
        next2.click()
        time.sleep(1)
        
        
       
        
# Function that its sole purpose is to unfollow the people you're following.  
def unfollow():
    time.sleep(1)
    profile = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')
    profile.click()
    time.sleep(2)
    unfollowers = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a")
    unfollowers.click()
    time.sleep(2)
    num = 1
    
    while num <= 80:
        try:
            if num == 12:
                unfollow_button = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li[" + str(num) + "]/div/div[3]/button")
                unfollow_button.click()
                time.sleep(1)
                unfollow_button = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li[" + str(num) + "]/div/div[3]/button")
                unfollow_button.click()
            
            unfollow_button = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li[" + str(num) + "]/div/div[3]/button")
            unfollow_button.click()
        
        except:
            time.sleep(1)
            unfollow_button = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li[" + str(num) + "]/div/div[2]/button")
            unfollow_button.click()
        
        final_unfollow = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]')
        final_unfollow.click()
        time.sleep(1)
        num += 1
        
        
    
       







