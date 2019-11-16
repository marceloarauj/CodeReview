# -*- coding: ISO-8859-1 -*-

import thread
import time, random

s1 = thread.allocate_lock()
s2 = thread.allocate_lock()

def tempo(i):
   t = random.randint(1,5)
   print "Processo %i dormindo por %i" %(i, t)
   time.sleep(t)

def thread1():
   print "Processo 1 - Adquirindo semáforo S1"
   s1.acquire()
   time.sleep(1)
   print "Processo 1 - Adquirindo semáforo S2"
   s2.acquire()
   print "Processo 1 - Seção crítica"
   tempo(1)
   print "Processo 1 - Liberando semáforos"
   s1.release()
   s2.release()
   print "Processo 1 - seção não crítica"
   tempo(1)

def thread2():
   print "Processo 2 - Adquirindo semáforo S2"
   s2.acquire()
   time.sleep(1)
   print "Processo 2 - Adquirindo semáforo S1"
   s1.acquire()
   print "Processo 2 - Seção crítica"
   tempo(2)
   print "Processo 2 - Liberando semáforos"
   s2.release()
   s1.release()
   print "Processo 2 - seção não crítica"
   tempo(2)

thread.start_new_thread(thread1, ())
thread.start_new_thread(thread2, ())

while 1: pass