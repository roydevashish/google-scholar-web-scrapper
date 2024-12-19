# https://scholar.google.com/scholar?start=0&q=allintitle:+%22image+encryption%22&hl=en&as_sdt=0,5
# https://scholar.google.com/scholar?start=30&q=%22chacha20%22+%2B+%22image+encryption%22&hl=en&as_sdt=0,5
# https://scholar.google.com/scholar?start=0&q=%22image+encryption%22+%2B+%22chacha20%22+%2B+%22ECC%22&hl=en&as_sdt=0,5

from bs4 import BeautifulSoup
import requests
import time

filename = input("File Name: ")
outputfile = open("results/Result - "+filename+".csv", "w")
idx_start_page = int(input("Input the starting page no: "))
idx_end_page = int(input("Input the ending page no: "))

for idx_page in range(idx_start_page-1, idx_end_page):
    for i in range(30):
        print("next request in:", 30 - i, "sec")
        time.sleep(1)
    print("running page no: " + str(idx_page+1))
    idx_link = str(idx_page * 10)
    link = "https://scholar.google.com/scholar?start=" + idx_link + "+&q=%22image+encryption%22+%2B+%22chacha20%22+%2B+%22ECC%22&hl=en&as_sdt=0,5"
    print("Sending request to Google Scholar.")
    res = requests.get(link)
    print("Received response from Google Scholar.")
    content = res.text
    
    soup = BeautifulSoup(content, "html.parser")
    rt_list = soup.find_all(class_="gs_rt")

    rt_counter = 1
    for idx_rt in rt_list:
        print("writing research title no: " + str((int(idx_link) + rt_counter)))
        rt_counter = rt_counter+1

        try:
            paper_title = idx_rt.text
            paper_link = idx_rt.find(name="a").get("href")
            output_string = paper_title + "|" + paper_link + "\n"
            outputfile.write(output_string)
        except:
            outputfile.write("\n")
        
print("Done")
outputfile.close()