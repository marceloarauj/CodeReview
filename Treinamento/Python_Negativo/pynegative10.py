ord_text = lambda n: "%d%s" % (n, "th" if 10 < n % 100 < 14 else {1:"st", 2:"nd", 3:"rd"}.get(n % 10, "th"))
