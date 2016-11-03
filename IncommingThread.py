# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:04:14 2016

@author: markus
"""

import mailbox

def IncommingThread (conn, REPLY, KNOWN):
    incomming = dict (data = False, rcpt = None, mlfr = None, msg = "")
    conn.send (REPLY["ready"])
    
    while True:
        data = conn.recv (1024)
        
        if not data:
            break
        
        data = data.decode()
        
        if incomming["data"]:
            
            incomming["msg"] += data
            print(incomming["msg"])

            # last line is only a . ? data transfer is finished
            # tias            
            # stop = data.split("\n")[-1].strip()
            if data.split("\n")[-1].strip() == "." or data.split("\n")[-2].strip() == ".":
                # todo: optional filter
                # todo: determine Maildir folder of mlfr
                md = mailbox.Maildir('/home/foo/Maildir')
                md.add(incomming["msg"])
                incomming["data"] = False
        
        elif data.find("DATA") == 0:
            # only accept data when rcpt and mlfr are known
            if incomming["rcpt"] is not None and incomming["mlfr"] is not None:
                incomming["data"] = True
                conn.send (REPLY["start"])
            else:
                break
            
        elif data.find("QUIT") == 0:
            break
        
        elif data.find("RCPT TO:") == 0:
            rcpt = data.split("RCPT TO:")[1].strip()
             # if RCPT is unknown, just quit connection immediately :)
            if rcpt in KNOWN:
                incomming["rcpt"] = rcpt
                conn.send (REPLY["ok"])
            else:               
                break
            
        elif data.find("HELO ") == 0 or data.find("EHLO") == 0:
            # HELO blabla, trust no one
            conn.send (REPLY["ok"])
            
        elif data.find("MAIL FROM:") == 0:
            mlfr = data.split("MAIL FROM:")[1].strip()
            incomming["mlfr"] = mlfr
            conn.send (REPLY["ok"])
            
        else:
            # dunno what you want...bye!
            break
            
       
    conn.send (REPLY["close"])
    conn.close ()
    return