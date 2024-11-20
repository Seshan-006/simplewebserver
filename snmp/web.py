form http.server import HTTPServer, BaseHTTPRequesthandler
content="""
<!doctype html>
<html>
    <body bgcolor="PURPLE">
        <table border="5" cellpadding="22" aling="center" bgcolor="cyan">
            <caption aling="center">LAPTOP CONFIGURATION </caption>
        
        <tr bgcolor="blue">
            <th>S.NO</th><th>SYSTEM CONFIGURATION</th><th>DESCRIPTION</th>
        </tr>
        <tr>
            <th>1</th><th>PROCESSOR</th><th>i5</th>
        </tr>
        <tr>
            <th>2</th><th>PRIMARY MEMORY</th><th>RAM 16GB</th>
        </tr>
        <TR>
            <th>3</th><th>SECONDARY MEMORY</th><th>512 GB</th>
        </TR>
        <tr>
            <th>4</th><th>OS</th><th>WINDOWS 11</th>
        </tr>
        <tr>
            <th>5</th><th>GRAPIC CARD</th><TH>NVIDIA</TH>
        </tr>
        </table>
    </body>    
</html>      
"""
class myhandler(baseHTTPRequesthandler):
    def do_GET(self):
        print("request recevied")
        self.send_response(200)
        self.send_headers('content-type','text/html;charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd =HTTPServer(server_address,myhandler)
print("my webserver is running...")
httod.serve_forever()