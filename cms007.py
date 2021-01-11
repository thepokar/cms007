import requests
from termcolor import colored
uu = []
links = []
logo = """

███████╗██╗     ██████╗  ██████╗ ██╗  ██╗███████╗██████╗
██╔════╝██║     ██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝██╔══██╗
█████╗  ██║     ██████╔╝██║   ██║█████╔╝ █████╗  ██████╔╝
██╔══╝  ██║     ██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
███████╗███████╗██║     ╚██████╔╝██║  ██╗███████╗██║  ██║
╚══════╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                   

"""
print(colored(logo,"red"))
print(colored("My Channel : https://www.youtube.com/channel/UCkmU73jmY7TFUEYF0OGMQFQ", 'blue'))
print(colored("My Github : https://github.com/thepokar", 'blue'))
print("\n")
xx = input("Enter Your Ip ===> ")
print("[1] Wordpress")
print("[2] Joomla")
print("[3] Magento")
print("[4] Drupal")
print("[5] Sites")
ww = input("Enter Your Choice ===> ")
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.3'}
oo = 20
kk = str(oo)+"0"
page = 0
while page <= int(kk)-10:
    qq = requests.get("http://www.bing.com/search?q=ip%3a+"+str(xx.strip())+"&first="+str(page),headers=headers)
    sp = str(qq.content)
    rr = len(sp.split('href="'))
    for ss in range(1,rr):
        results = sp.split('href="')[ss]
        result = results.find('"')
        if "http" not in str(results[:result]) or "microsoft" in str(results[:result]):
            pass
        else:
            links.append(str(results[:result]))
    page +=10

if ww == "1":
    for link in links:
        zz = link.find("/", 8)
        if str(link[:zz+1]) not in uu:
            uu.append(str(link[:zz+1]))
            try:
                req = requests.get(str(link[:zz+1]) + "wp-login.php")
                if "wp-submit" in str(req.content.lower()):
                    print(str(link[:zz+1]))
                else:
                    pass
            except:
                pass
elif ww == "2":
    for link in links:
        zz = link.find("/", 8)
        if str(link[:zz+1]) not in uu:
            uu.append(str(link[:zz+1]))
            try:
                req = requests.get(str(link[:zz+1]) + "administrator")
                if "joomla" in str(req.content.lower()):
                    print(str(link[:zz+1]))
                else:
                    pass
            except:
                pass
elif ww == "3":
    for link in links:
        zz = link.find("/", 8)
        if str(link[:zz+1]) not in uu:
            uu.append(str(link[:zz+1]))
            try:
                req = requests.get(str(link[:zz+1]) + "errors/design.xml")
                if req.status_code == 200 and 'magento' in req.text.lower() and "404" not in req.text:
                    print(str(link[:zz+1]))
                else:
                    pass
            except:
                pass
elif ww == "4":
    for link in links:
        zz = link.find("/", 8)
        if str(link[:zz+1]) not in uu:
            uu.append(str(link[:zz+1]))
            try:
                req = requests.get(str(link[:zz+1]))
                if req.status_code == 200 and 'name="Generator" content="Drupal' in req.text:
                    print(str(link[:zz+1]))
                else:
                    pass
            except:
                pass



elif ww == "5":
    for link in links:
        zz = link.find("/", 8)
        if str(link[:zz+1]) not in uu:
            uu.append(str(link[:zz+1]))
            try:
                req = requests.get(str(link[:zz+1]) + "administrator")
                if "joomla" in str(req.content.lower()):
                    pass
                else:
                    req = requests.get(str(link[:zz+1]) + "wp-login.php")
                    if "wp-submit" in str(req.content.lower()):
                        pass
                    else: 
                        req = requests.get(str(link[:zz+1]) + "errors/design.xml")
                        if req.status_code == 200 and 'magento' in req.text.lower() and "404" not in req.text:
                            pass
                        else:
                            req = requests.get(str(link[:zz+1]))
                            if req.status_code == 200 and 'name="Generator" content="Drupal' in req.text:
                                pass
                            else:
                                print(str(link[:zz+1]))
            except:
                pass
