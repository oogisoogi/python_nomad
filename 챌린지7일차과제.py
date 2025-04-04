# 샐행 중 아래 에러 발생 => 텍스트 추출 메소드가 문제를 일으킴
# 노력했으나 해결하지 못하고 제출함
# 언어 개별적으로는 추출이 되지만, 에러로 인해 연속으로 추출하는 것은 실패
#
# == 에러 메시지 ==
# Traceback (most recent call last):
#   File "d:\python\챌린지7일차과제.py", line 39, in <module>
#     company = job_py.find("a", class_="bjs-jlid__b").text
#               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'NoneType' object has no attribute 'text'


import requests
from bs4 import BeautifulSoup

response_py = requests.get(
    "https://berlinstartupjobs.com/skill-areas/python/",
    headers={
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })

response_ts = requests.get(
    "https://berlinstartupjobs.com/skill-areas/typescript/",
    headers={
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })

response_js = requests.get(
    "https://berlinstartupjobs.com/skill-areas/javascript/",
    headers={
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })

response_eg = requests.get(
    "https://berlinstartupjobs.com/engineering/",
    headers={
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })


#Python 추출
print(f"=====================\n  Python Job  \n=====================\n")
soup_py = BeautifulSoup(response_py.content, "html.parser") 
jobs_py = soup_py.find("div", id="content").find_all("li")

for job_py in jobs_py:
    company = job_py.find("a", class_="bjs-jlid__b").text
    title = job_py.find("h4", class_="bjs-jlid__h").text
    description = job_py.find("div", class_="bjs-jlid__description").text.strip()
    link = job_py.find("a")["href"]
    print(f"회사명: {company}\n모집 영역: {title}\n직무 링크: {link}\n직무 설명: {description}\n\n\n")


#Typescript 추출
print(f"=====================\n  Typescript Job  \n=====================\n")
soup_ts = BeautifulSoup(response_ts.content, "html.parser") 
jobs_ts = soup_ts.find("div", id="content").find_all("li")

for job_ts in jobs_ts:
    company = job_ts.find("a", class_="bjs-jlid__b").text
    title = job_ts.find("h4", class_="bjs-jlid__h").text
    description = job_ts.find("div", class_="bjs-jlid__description").text.strip()
    link = job_ts.find("a")["href"]
    print(f"회사명: {company}\n모집 영역: {title}\n직무 링크: {link}\n직무 설명: {description}\n\n\n")


#Javascript 추출
print(f"=====================\n  Javascript Job  \n=====================\n")
soup_js = BeautifulSoup(response_js.content, "html.parser") 
jobs_js = soup_js.find("div", id="content").find_all("li")

for job_js in jobs_js:
    company = job_js.find("a", class_="bjs-jlid__b").text
    title = job_js.find("h4", class_="bjs-jlid__h").text
    description = job_js.find("div", class_="bjs-jlid__description").text.strip()
    link = job_js.find("a")["href"]
    print(f"회사명: {company}\n모집 영역: {title}\n직무 링크: {link}\n직무 설명: {description}\n\n\n")


#Engneering 추출
print(f"=====================\n  Engineering Job  \n=====================\n")
soup_eg = BeautifulSoup(response_eg.content, "html.parser") 
jobs_eg = soup_eg.find("div", id="content").find_all("li")

for job_eg in jobs_eg:
    company = job_eg.find("a", class_="bjs-jlid__b").text
    title = job_eg.find("h4").text
    description = job_eg.find("div", class_="bjs-jlid__description").text.strip()
    link = job_eg.find("a")["href"]
    print(f"회사명: {company}\n모집 영역: {title}\n직무 링크: {link}\n직무 설명: {description}\n\n\n")