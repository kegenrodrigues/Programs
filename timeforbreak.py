import time
from selenium import webdriver


total_breaks = 4
break_count = 0

print("This program started on "+time.ctime())#prints current time

while (break_count < total_breaks):
    #path set in environment variables "V:\Kegen\Softwares\chromedriver.exe"
    driver = webdriver.Chrome("V:\Kegen\Softwares\chromedriver.exe")#path of webdriver is now set in environment variables
    #url="https://www.youtube.com/watch?v=f6vY6tYvKGA"
    url="https://www.youtube.com/watch?v=6H2oKfqSZq0"
    driver.get(url)
    print("Break Number "+str(break_count)+" started at "+time.ctime())
    time.sleep(220)#take break for this many seconds
    driver.close()
    print("Break Number "+str(break_count)+" ended at "+time.ctime())
    print("Start your work")
    time.sleep(5)#Dont take break for this many seconds
    
    break_count += 1
    
