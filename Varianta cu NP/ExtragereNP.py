# -*- coding: utf-8 -*-
import requests
import xml.etree.ElementTree as ET
import codecs
import docx2txt
import numpy

import codecs


a=docx2txt.process("TextInput.docx")

a=a.replace(u'“', '')
a=a.replace(u'”', '')


request = u"""<?xml version="1.0" encoding="utf-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webNpChunkerRo.uaic/">
   <soapenv:Header/>
   <soapenv:Body>
      <web:chunkText>
         <inputText>""" + a + u"""</inputText>
      </web:chunkText>
   </soapenv:Body>
</soapenv:Envelope>"""

encoded_request = request.encode('utf-8')

headers = {"Host": "www.webNpChunkerRo.uaic",
           "Content-Type": "text/xml; charset=UTF-8",
           "Content-Length": str(len(encoded_request))}

response = requests.post(url="http://nlptools.info.uaic.ro/WebNpChunkerRo/NpChunkerRoWS?wsdl",
                         headers=headers,
                         data=encoded_request,
                         verify=False)


def unescape(s):
    s = s.replace("&lt;", "<")
    s = s.replace("&gt;", ">")
    s = s.replace("&amp;", "&")
    s = s.replace("&quot;", "\"")
    s = s.replace('"no"?>', " ")
    return s

m=(unescape(response.text))[229:-55]


with codecs.open("outputAdNP.xml", "w", "utf-8-sig") as temp:
    temp.write(m)

