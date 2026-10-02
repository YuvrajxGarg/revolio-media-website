"""Local static preview with byte-range support for HTML5 video."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os,re

class Handler(SimpleHTTPRequestHandler):
    protocol_version='HTTP/1.1'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,directory=str(Path(__file__).parent/'dist'),**kwargs)
    def end_headers(self):
        self.send_header('Accept-Ranges','bytes')
        self.send_header('Cache-Control','no-cache')
        super().end_headers()
    def send_head(self):
        self.remaining=None
        path=self.translate_path(self.path)
        request=self.headers.get('Range')
        if not request or not os.path.isfile(path):return super().send_head()
        size=os.path.getsize(path)
        match=re.fullmatch(r'bytes=(\d*)-(\d*)',request.strip())
        try:
            if not match or not any(match.groups()):raise ValueError()
            a,b=match.groups()
            if not a:
                amount=int(b)
                if amount<=0:raise ValueError()
                start=max(0,size-amount);end=size-1
            else:
                start=int(a);end=min(int(b) if b else size-1,size-1)
            if start>=size or start>end:raise ValueError()
        except ValueError:
            self.send_response(416)
            self.send_header('Content-Range',f'bytes */{size}')
            self.send_header('Content-Length','0')
            self.end_headers();return None
        stream=open(path,'rb');stream.seek(start)
        self.remaining=end-start+1
        self.send_response(206)
        self.send_header('Content-Type',self.guess_type(path))
        self.send_header('Content-Range',f'bytes {start}-{end}/{size}')
        self.send_header('Content-Length',str(self.remaining))
        self.send_header('Last-Modified',self.date_time_string(os.path.getmtime(path)))
        self.end_headers();return stream
    def copyfile(self,source,outputfile):
        try:
            if self.remaining is None:return super().copyfile(source,outputfile)
            remaining=self.remaining
            while remaining:
                data=source.read(min(128*1024,remaining))
                if not data:break
                outputfile.write(data);remaining-=len(data)
        except (BrokenPipeError,ConnectionResetError):pass
    def log_message(self,format,*args):pass

if __name__=='__main__':
    print('Revolio preview: http://127.0.0.1:4173',flush=True)
    ThreadingHTTPServer(('127.0.0.1',4173),Handler).serve_forever()
