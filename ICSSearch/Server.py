import string,cgi,time,urllib,json
from io import open
from urlparse import urlparse,parse_qs
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
import sys
from threading import *

import DocFetcher, admin

class QueryHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            parsed = urlparse(self.path)
            queries = parse_qs(parsed.query)
            hasResp = False
            if "as" in queries and queries["as"][0] == "true":
                #auto suggest part
                if "q" in queries:
                    jsonResp = json.dumps(DocFetcher.GetASResult(queries["q"][0]))
                    hasResp = True
            elif "q" in queries:
                #normal query part
                jsonResp = json.dumps(DocFetcher.GetResult(queries["q"][0]))
                hasResp = True
            if hasResp:    
                self.send_response(200)
                self.send_header('Content-type','application/json')
                self.send_header("Access-Control-Allow-Origin", "*");
                self.send_header("Access-Control-Expose-Headers", "Access-Control-Allow-Origin");
                self.send_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
                self.end_headers()
                self.wfile.write(jsonResp)
            else:
                if parsed.path != "" and not "favicon" in parsed.path:
                    self.send_response(200)
                    print(parsed.path)
                    if (parsed.path.endswith(".js")):
                        contenttype = "application/javascript"
                        path = "../FinalSet/Webpage" + parsed.path
                    elif (".css" in parsed.path):
                        contenttype = "text/css"
                        path = "../FinalSet/Webpage" + parsed.path
                    else:
                        contenttype = "text/html"
                        path = "../FinalSet/Webpage/index.html"
                    self.send_header('Content-type',contenttype)
                    self.end_headers()
                    indexfile = open(path, "rb")
                    self.wfile.write(indexfile.read())
                    indexfile.close()
                else:
                    self.send_response(200)
                    self.send_header('Content-type','text/html')
                    self.end_headers()
                    indexfile = open("../FinalSet/Webpage/index.html", "r")
                    self.wfile.write(indexfile.read())
                    indexfile.close()
        except IOError:
            self.send_error(404,'What Shady Shit was tried?')

def DataLoader():
    DocFetcher.LoadTrie()
    DocFetcher.docidLoader()

def main(port):
    try:
        server = HTTPServer(('', port), QueryHandler)
        print 'Loading up Awesome server.'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Bye Bye'
        server.socket.close()

if __name__ == '__main__':
    #if not admin.isUserAdmin():
    #    admin.runAsAdmin()
    port = 80
    if ('PORT' in os.environ):
        port = int(os.environ['PORT'])
    print(sys.argv)
    Thread(target = DataLoader, args=()).start()
    main(port)