with open('packets_filtered.txt', 'r') as f:
    data = f.read()

chunks = data.split('\n\n')

keypresses = []

switcher = {
    "04": "a",  # or A
    "05": "b",  # or B
    "06": "c",  # or C
    "07": "d",  # or D
    "08": "e",  # or E
    "09": "f",  # or F
    "0A": "g",  # or G
    "0B": "h",  # or H
    "0C": "i",  # or I
    "0D": "j",  # or J
    "0E": "k",  # or K
    "0F": "l",  # or L
    "10": "m",  # or M
    "11": "n",  # or N
    "12": "o",  # or O
    "13": "p",  # or P
    "14": "q",  # or Q
    "15": "r",  # or R
    "16": "s",  # or S
    "17": "t",  # or T
    "18": "u",  # or U
    "19": "v",  # or V
    "1A": "w",  # or W
    "1B": "x",  # or X
    "1C": "y",  # or Y
    "1D": "x",  # or Z
    "1E": "1",  # or !
    "1F": "2",  # or @
    "20": "3",  # or #
    "21": "4",  # or $
    "22": "5",  # or %
    "23": "6",  # or ^
    "24": "7",  # or &
    "25": "8",  # or *
    "26": "9",  # or (
    "27": "0",  # or )
    "2D": "-",  # or _
    "2E": "+",  # or =
    "2F": "[",  # or {
    "30": "]",  # or }
    "31": '"',  # or |
    "33": ";",  # or :
    "34": "'",  # or "
    "35": "`",  # or ~
    "36": ",",  # or <
    "37": ".",  # or >
    "38": "/",  # or ?
}


usb_codes = {
	0x04:"aA", 0x05:"bB", 0x06:"cC", 0x07:"dD", 0x08:"eE", 0x09:"fF",
	0x0A:"gG", 0x0B:"hH", 0x0C:"iI", 0x0D:"jJ", 0x0E:"kK", 0x0F:"lL",
	0x10:"mM", 0x11:"nN", 0x12:"oO", 0x13:"pP", 0x14:"qQ", 0x15:"rR",
	0x16:"sS", 0x17:"tT", 0x18:"uU", 0x19:"vV", 0x1A:"wW", 0x1B:"xX",
	0x1C:"yY", 0x1D:"zZ", 0x1E:"1!", 0x1F:"2@", 0x20:"3#", 0x21:"4$",
	0x22:"5%", 0x23:"6^", 0x24:"7&", 0x25:"8*", 0x26:"9(", 0x27:"0)",
	0x2C:"  ", 0x2D:"-_", 0x2E:"=+", 0x2F:"[{", 0x30:"]}",  0x32:"#~",
	0x33:";:", 0x34:"'\"",  0x36:",<",  0x37:".>", 0x28: '\n\n', 0x38: '/?', 0x2b: '\t\t'
	}

caps_lock = False
inputs = ''
for chunk in chunks:
    data = ''
    for line in chunk.splitlines():
        line = line.strip()
        line_data = line.split('  ')[1].replace(' ', '')
        data += line_data
    data_slice = data[-16:]
    code = int(data_slice[4:6], 16)
    if code == 0:
        continue
    if code == 0x2a:
        inputs = inputs[:-1]
    elif code == 0x39:
        #caps_lock = True
        pass
    else:
        try:
            shift_pressed = int(data_slice[0:2],16) == 2
            if caps_lock:
                if shift_pressed:
                    is_cap = 0
                else:
                    is_cap = 1
            else:
                if shift_pressed:
                    is_cap = 1
                else:
                    is_cap = 0
            inputs += usb_codes[code][is_cap]
        except:
            print('missing code', hex(code))
            exit(0)
print(inputs)

#bctf{St0p_s3nd1Ng_m3_DuCK_p1c$}
