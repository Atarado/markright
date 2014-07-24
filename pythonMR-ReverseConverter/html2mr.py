#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This example is simple html to markright converting; it converts atarado.html file
to atarado_out.mr - markright file. Script is the most simple, without sys.argv 
for entering arguments from terminal.
"""
import re
from HTMLParser import HTMLParser

data=None
with open('atarado.html', 'r') as f :
    data = f.read()


out = open( "atarado_out.mr", 'wb' )
out.write( 
"""#!/usr/bin/markright
# -*- coding: utf-8 -*-
""" )

n="\n"
s=" "
z=","

class Parser(HTMLParser):
    t = None
    indent=-1
    
    def handle_starttag(self, tag, attrs):
        
        self.indent+=1
        self.t = tag
        if tag == "br" :
            out.write( n + s*self.indent*2 + tag + s)
        
        else :
            out.write( n + s*self.indent*2 + tag[0].upper() + tag[1:] + s)
        
        if attrs :
            out.write( "( " )
            
            for a in attrs :
                
                if attrs[-1] is a :
                    out.write( a[0] +s+ a[1] +s )
                else :
                    out.write( a[0] +s+ a[1] +z +s )
                    
            out.write( ") " )
        
    def handle_endtag(self, tag):
        
        if tag == "br" :
            pass
        elif tag == self.t :
            out.write( tag )
        else :
            out.write( n + s*self.indent*2 + tag )
        
        self.indent-=1
    
    def handle_data(self, data):
        
        if not data.isspace() :
            data = " ".join( data.split() )
            out.write( data + ',, ' )
    
    def handle_comment(self, data):
        
        out.write( n + s*2 + s*self.indent*2 + ".- " + data + " -." )


def doctype() :
    
    dType = re.match( r'<!DOCTYPE.*?>', data, re.U )
    
    if dType :
        out.write( n + ",," + dType.group() + ",," )
        
        return data.index( dType.group()[-1] )
        
datapos = doctype()    

parser = Parser()
parser.feed( data )

out.close()
