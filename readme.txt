Sebastian Susanto
INFO-I 427
Fall 2018

Algorithm
Step 1) Ask the user for a url
*You need to have a formatted url such as https://www.indiana.edu/ with https:// and have a "/" at the very end of the link
#So all links need to be start be like this: https://{link}/

Step 2) Ask users for path, methods to pick (dfs or bfs), and jumps (how many files you wan to grab)

#Ask for path, do a complete path like /Users/sebastiansusanto/Documents/webCrawler (mac)
#The path might be different if you use windows
#The jumps should be an integer

Step 3) crawler function takes two argument: the first url and path
#The crawler first opens the url, grabs the content, and writes it down in a .txt file with numbers marked on it
#The numbers starts at 0. So if you are running asking the function to grab 50 pages, it will return 51 pages including the seed url
#Adds it into a dictionary for the index.dat purposes (a reference to all the files and links)
#Filter out links so that it is unique, has html file, and is approved by robots.txt
#To get approved by robots.txt, I obtain the seed url, meaning no extension, and add robots.txt and use robotparser to validate
#Now I have a list that contains links. I add it into the deque

Step 4) Next, I run a for loop that runs as many times as the user requestion, and runs the crawlerMethod() function
#crawlerMethod function is similar to crawler, the only difference is that it consists of the crawling algorithm of either bfs or dfs
#If its a bfs, I pop left, if its a dfs, I pop right, to obtain the next link
#Crawl into that link, and grabs all the validated links, and append it into the deque
#If the deque runs out before the loop ends, I break the loop

Step 5) Create a index.dat file that lists down the file name and the links it references
#Reindex the dictionary to reformat it as file_number:links it was referring to

Sample process would be

url : https://www.indiana.edu/
path: /Users/sebastiansusanto/Documents/webCrawler/bfs
or
path: /Users/sebastiansusanto/Documents/webCrawler/dfs
method: bfs
or method: dfs
jumps: 50