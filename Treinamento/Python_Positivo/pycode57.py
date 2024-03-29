#  ___ GPr Sistemas ____________________________________
#
#  Modulo: gpmail.py
#  Data de Criação:     2003-02-26
#  Data de Atualização: 2003-12-05
#
#  Desenvolvedores: João Chaves/Rod Senra
#  Interpretador:   Python 2.3.2  ou superior

import sys
import smtplib
import MimeWriter
import mimetypes
import base64
import StringIO
import getopt
import os.path
import sys
import urllib2
from StringIO import StringIO
from Crypto.Cipher import DES   # Opcional
from syslog import *
from traceback import format_exception


__version__ = '0.4'


# Configurações

# alterar aqui com nome ou endereço servidor smtp
__server = '127.0.0.1'  

# Atualmente  nao esta havendo autenticacao, preencha 
# se necessario
__login = ""
__passwd = ""


def attachText(_writer, _text,_mime):
    part = _writer.nextpart()
    body = part.startbody(_mime)
    body.write(_text)



def attachPlainFile(_writer, _file, _mimeType=None,
                    _name="unknown"):
    part = _writer.nextpart()
    part.addheader('Content-Transfer-Encoding','base64')
    body = part.startbody("%s; name=%s"%(_mimeType,_name))
    base64.encode(StringIO(_file),body)

    

def attachCryptFile(_writer, _file,_mimeType=None,
                    _name="unknown"):
    part = _writer.nextpart()
    part.addheader('Content-Transfer-Encoding', 'base64')
    body = part.startbody('%s; name=%s'%(_mimeType,_name))
    obj = DES.new(" secret ",DES.MODE_ECB)
    pad = 8-(len(_file)%8)
    _file = _file+pad*" "
    crypt = obj.encrypt(_file)
    base64.encode(StringIO(crypt),body)

    



def sendmail(_subject,_from,_to,_cc=None,_attachments=None):
    try:
        message = StringIO()
        writer = MimeWriter.MimeWriter(message)
        writer.addheader('MIME-Version', '1.0')
        writer.addheader('Subject', _subject)
        writer.addheader('To',_to)

        if _cc:
            writer.addheader('Cc',_cc)

        writer.startmultipartbody('mixed')

        

        # process attachments
        if _attachments:
            for _mode,_file,_mime,_name in _attachments:
                if _mode=="text":
                    attachText(writer,_file.read(),_mime)
                elif _mode=="attach":
                    attachPlainFile(writer,_file.read(),
                                    _mime,_name)
                elif _mode=="crypt":
                    attachCryptFile(writer,_file.read(),
                                    _mime,_name)        
                else:
                    raise Exception("Invalid Mode specified")

        # finish off
        writer.lastpart()

        # send the mail
        smtp = smtplib.SMTP(__server)

        # Uncomment the line below if you need authentication

        if __login:
            smtp.login(__login,__passwd)


        smtp.sendmail(_from,_to, message.getvalue())
        #print message.read()

        smtp.quit()
        syslog(LOG_INFO,"Email Ok")

    except:
        syslog(LOG_INFO,
               str(format_exception(sys.exc_info()[0],
                                    sys.exc_info()[1],
                                    sys.exc_info()[2])))