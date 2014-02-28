import string,cgi,time,urllib,json
from io import open
from urlparse import urlparse,parse_qs
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

import DocFetcher, admin

class QueryHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            queries = parse_qs(urlparse(self.path).query)
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
        except IOError:
            self.send_error(404,'What Shady Shit was tried?')

def main():
    try:
        server = HTTPServer(('', 4444), QueryHandler)
        print 'Loading up Awesome server.'
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Bye Bye'
        server.socket.close()

if __name__ == '__main__':
    if not admin.isUserAdmin():
        admin.runAsAdmin()
    DocFetcher.LoadTrie()
    DocFetcher.docidLoader()
    main()