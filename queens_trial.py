from urllib.request import urlopen 
import certifi
import ssl

context = ssl.create_default_context(cafile=certifi.where())

url = "https://www.queensu.ca/admission/applying/competitive-average"
page = urlopen(url, context=context)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)

start_index = html.find("<Smith School of Buisness COmmerce (QC)>")
print("smith index", start_index)

#if range != -1:
if True:
#this creates a condition for the search operation i made here
    acceptance_start = html.find("High School Percentage Grade")
    #this is going to look for a string in html and returns the postion of the string 
    print(acceptance_start)
    if acceptance_start != -1:
    #if its not out of range it will look for the acceptance rate of the school 
        acceptance_end = html.find("<", acceptance_start)
        acceptance_rate = html[acceptance_start:acceptance_end]    
        print(f"Smith school acceptnce: {acceptance_rate}")
    
    else:
        print("womp womp")
else:
    print("boooooooooo")
#if the very first condition is not true then this will display on the screen

