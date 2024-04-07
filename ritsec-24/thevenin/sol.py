# https://www.youtube.com/watch?v=zTDgziJC-q8

#(pow(((1/10) + (1/3)), -1) + 2)
#4.3076923076923075
rth = (pow(((1/10) + (1/3)), -1) + 2)
# (((40 - vc)/10) + 5 - ((vc - 0)/3) == 0)
# 270 - 13*vc == 0

vc = 270/13
il = vc/(rth+2.7)
print(hash(round(il, 2)))
# RS{2213609288845146114}
