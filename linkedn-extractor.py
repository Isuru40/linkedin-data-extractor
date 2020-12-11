import time
from selenium import webdriver
import os
import csv

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["No", "Name", "Tag-line","Top-skils","Other-skils"])
    
    options = webdriver.ChromeOptions()
    CHROMEDRIVER_PATH = 'chromedriver.exe'
    GOOGLE_CHROME_SHIM = os.getenv('GOOGLE_CHROME_SHIM', "chromedriver")

    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)

    
    profilesToProcess = ['kumuditha-gimnath-387a83149','i-d-r','nsa94']
    no = 0

    browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    
    # Wait 1 seconds for the page to load and log in
    time.sleep(1)

    browser.execute_script("document.getElementsByTagName('input')[1].value = 'example@gmail.com';")
    browser.execute_script("document.getElementsByTagName('input')[15].value = 'put-password-of-linkdnaccount';")
    browser.execute_script("document.getElementsByTagName('button')[0].click();")
    time.sleep(5)

    for profile in profilesToProcess:
        weburl = 'https://www.linkedin.com/in/'+ profile + '/';
        browser.get(weburl)
        time.sleep(2)
        name= browser.execute_script("return (function(){try{return document.getElementsByClassName('break-words')[0].innerText; } catch(e){return 0;}})()")
        print(name)
        time.sleep(1)
        tagline= browser.execute_script("return (function(){try{return document.getElementsByClassName('break-words')[1].innerText; } catch(e){return 0;}})()")
        print(tagline)
        time.sleep(1)
        browser.execute_script(" var elmnt = document.querySelector('.pv-highlights-section'); elmnt.scrollIntoView(); ")
        len_0= browser.execute_script("return (function(){try{var elmnt = document.querySelector('.pab-featured-section '); elmnt.scrollIntoView(); return 1;} catch(e){return 0;}})()")
        time.sleep(1)
        browser.execute_script(" var elmnt = document.querySelector('.pv-profile-section-pager '); elmnt.scrollIntoView(); ")
        time.sleep(1)
        len_1= browser.execute_script("return (function(){try{var elmnt = document.getElementById('experience-section'); elmnt.scrollIntoView(); return 1;} catch(e){return 0;}})()")
        time.sleep(1)
        len_2= browser.execute_script("return (function(){try{var elmnt = document.getElementById('education-section'); elmnt.scrollIntoView(); return 1;} catch(e){return 0;}})()")
        time.sleep(1)
        len_2= browser.execute_script("return (function(){try{var elmnt = document.getElementById('certifications-section'); elmnt.scrollIntoView(); return 1;} catch(e){return 0;}})()")
        time.sleep(1)
        len_3= browser.execute_script("return (function(){try{var elmnt = document.querySelector('.volunteering-section '); elmnt.scrollIntoView(); return 1;} catch(e){return 0;}})()")
        time.sleep(1)
        browser.execute_script(" var elmnt = document.querySelector('.pv-skill-categories-section'); elmnt.scrollIntoView(); ")
        time.sleep(3)
       
        len_= browser.execute_script("return (function(){try{return document.getElementsByClassName('pv-skill-category-entity__name-text').length;} catch(e){return 0;}})()")
        print(len_)
        skill_list = browser.execute_script("return (function(){ try{var s=document.getElementsByClassName('pv-skill-category-entity__name-text').length; var arr = []; for(c=0;c<(s);c++){ arr.push(document.getElementsByClassName('pv-skill-category-entity__name-text')[c].innerText); } return arr;} catch(e){return 0;}})()") 
        print(array)
        time.sleep(4)
        writer.writerow([no,name,tagline,skill_list[0:3],skill_list[3:]])
        no = no + 1 
   