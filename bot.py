from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


#gets the instagram page
driver =  webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.instagram.com/")
time.sleep(1)
driver.maximize_window()

# a Function that logs you into the account and in case instagram blocks you and asks for a password from your e-mail the Function will do it as well .
# all you have to do is wait. (in order to opreate the Function will require 2 fields to fill : 1.username of instagram(line 19 in file bot.py),  2.pass of instagram(line 21 in file bot.py),


def login():
    login_element = driver.find_element_by_name("username")
    login_element.send_keys("username-here")
    password_element = driver.find_element_by_name("password")
    password_element.send_keys("pass-here")
    password_element.send_keys(Keys.RETURN)
    time.sleep(3)
    savecancel = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div/div[2]/img')
    savecancel.click()
    time.sleep(2)
    cancel_button = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    cancel_button.click()
        

# follows your suggestions        
def follow_sugg():
    time.sleep(2)
    profile = driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div[3]/div[3]/div[1]/a/div")
    profile.click()
    time.sleep(1)
    num = 1
    while num <= 35:
        follow_button = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[2]/div/div/div[" + str(num) + "]/div[3]/button")
        follow_button.click()
        num += 1
        time.sleep(0)
    back = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div/div[2]/img')
    back.click()
        
   
# likes posts in an hashtag (1 field is required line 111 in file bot.py [without the "#" the Function will add it by itself])
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
    for pic in pics :
        pic.click()
        time.sleep(2)
        like = driver.find_element_by_class_name('fr66n')
        like.click()
        time.sleep(1)
        driver.back()
        time.sleep(1)
        
       
        
# Function that its sole purpose is to unfollow the people you following.  
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
        
        
    
       
login()
follow_sugg()
unfollow()
like_ph_hashtag("your hashtag here [without the #]")







