from collections import deque
import urllib.request, re, urllib.robotparser, os, time


#Constant Variable
links_to_crawl = deque([])
dictionary = {}
counter = 0

visited_url_lists = []

def crawler(url, path):
    global counter
    #Opens the URL and downloaded it
    page = urllib.request.urlopen(url)
    html_content = page.read().decode(errors="replace")

    #Mark down visited URL
    visited_url_lists.append(url)

    #Download the content and create a file into path
    os.chdir(path)
    file = open(str(counter)+".txt", "w")
    file.write(html_content)
    file.close

    #Adds into dictionary for indexing
    dictionary[counter] = url
    counter += 1

    #Find all the href links
    links = re.findall('(?<=a href=").+?(?=")', html_content)
    
    #Only grab HTML Pages
    html_links = []
    for item in links:
        if ".html" in item:
            html_links.append(item)
        
    #Removes Duplicate Sites
    final_list = []
    for item in html_links:
        if item not in final_list:
            final_list.append(item)
            
    base_url = re.search('(?<=https://).+?(?=/)', url)
    seed = base_url.group(0)
    
    #Initialize RobotParser
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url("https://"+ seed + "/robots.txt")
    rp.read()
    
    for item in final_list:
        value = rp.can_fetch("*", item)
        if value == False:
            final_list.remove(item)
            
        links_to_crawl.append(item)
        
            
            
def crawlerMethod(method):
    global counter
    #Crawler Politeness, wait for 1 second
    time.sleep(1)
    
    #depth-first search
    if method.lower() == "dfs":
        url = links_to_crawl.pop()
        #Opens the URL and downloaded it
        page = urllib.request.urlopen(url)
        html_content = page.read().decode(errors="replace")
        
        #Mark down visited URL
        visited_url_lists.append(url)
    
        #Download the content and create a file into path
        os.chdir(path)
        file = open(str(counter)+".txt", "w")
        file.write(html_content)
        file.close

        #Adds into dictionary for indexing
        dictionary[counter] = url
        counter += 1
    
        #Find all the href links
        links = re.findall('(?<=a href=").+?(?=")', html_content)
        
        #Only grab HTML Pages
        html_links = []
        for item in links:
            if ".html" in item:
                html_links.append(item)
            
        #Removes Duplicate Sites
        final_list = []
        for item in html_links:
            if item not in final_list:
                final_list.append(item)
                
        base_url = re.search('(?<=https://).+?(?=/)', url)
        seed = base_url.group(0)
        
        #Initialize RobotParser
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url("https://"+ seed + "/robots.txt")
        rp.read()
        
        for item in final_list:
            value = rp.can_fetch("*", item)
            if value == False:
                final_list.remove(item)
                
            links_to_crawl.appendleft(item)
        

    #breadth-first search
    if method.lower() == "bfs":
        url = links_to_crawl.popleft()
        #Opens the URL and downloaded it
        page = urllib.request.urlopen(url)
        html_content = page.read().decode(errors="replace")
        
        #Mark down visited URL
        visited_url_lists.append(url)
    
        #Download the content and create a file into path
        os.chdir(path)
        file = open(str(counter)+".txt", "w")
        file.write(html_content)
        file.close

        #Adds into dictionary for indexing
        dictionary[counter] = url
        counter += 1
    
        #Find all the href links
        links = re.findall('(?<=a href=").+?(?=")', html_content)
        
        #Only grab HTML Pages
        html_links = []
        for item in links:
            if ".html" in item:
                html_links.append(item)
            
        #Removes Duplicate Sites
        final_list = []
        for item in html_links:
            if item not in final_list:
                final_list.append(item)
                
        base_url = re.search('(?<=https://).+?(?=/)', url)
        seed = base_url.group(0)
        
        #Initialize RobotParser
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url("https://"+ seed + "/robots.txt")
        rp.read()
        
        for item in final_list:
            value = rp.can_fetch("*", item)
            if value == False:
                final_list.remove(item)
                
            links_to_crawl.append(item)
    
    
    
#main
url = input("Please enter the a url to crawl: ")
path = str(input("Please enter the name of a directory in which to save the crawled pages: "))
method = input("Which crawling algorithm would you like (dfs or bfs): ")
jumps = eval(input("Please enter the maximum number of pages to crawl (an integer): "))

crawler(url, path)
for i in range(jumps):
    #If the links to crawl ran out before the foor loop ends, break it
    if len(links_to_crawl) == 0:
        break
    crawlerMethod(method)

#Create index.dat that lists the mapping between the URLs and the filenames you’ve assigned locally
os.chdir(path)
content = ""
for item in dictionary:
    content += str(item) +  ':' + dictionary[item] + "\n"

with open("index.dat", "w") as file:
    file.write(content)

#print(content)



#Test Code
#https://www.indiana.edu/
#/Users/sebastiansusanto/Documents/webCrawler

