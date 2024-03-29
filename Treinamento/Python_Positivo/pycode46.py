#!/usr/bin/python
#
# limitget.py
# Copyright (c) 2006 by Nilton Volpato <first-name dot last-name @ gmail.com>
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose and without fee is hereby granted,
# provided that the above copyright notice appear in all copies and that
# both that copyright notice and this permission notice appear in
# supporting documentation.
#
# This file is provided AS IS with no warranties of any kind.  The author
# shall have no liability with respect to the infringement of copyrights,
# trade secrets or any patents by this file or any part thereof.  In no
# event will the author be liable for any lost revenue or profits or
# other special, indirect and consequential damages.

import urllib
import time
from progressbar import ProgressBar, Bar, ETA, Percentage, FileTransferSpeed

def limitget(url, outfname, limit):
    """Downloads an url to a local file using a bandwidth limit.
    url: resource to download
    outfname: filename to which url will be copied
    limit: bandwidth limit in bytes/second
    """
    fp = urllib.urlopen(url)
    op = open(outfname, 'wb')
    n = 0
    widgets = [Percentage(), ' ', Bar(),' ', ETA(), ' ', FileTransferSpeed()]
    size = int(fp.headers['content-length'])
    pbar = ProgressBar(widgets=widgets, maxval=size).start()
    while 1:
        start = time.time()
        s = fp.read(limit)
        if not s:
            break
        op.write(s)
        n += len(s)
        timetosleep = 1.0 - (time.time() - start)
        if timetosleep > 0.0:
            time.sleep(timetosleep)
        pbar.update(n)
    pbar.finish()
    fp.close()
    op.close()

if __name__ == '__main__':
    import sys
    limitget(sys.argv[1], sys.argv[2], int(sys.argv[3]))