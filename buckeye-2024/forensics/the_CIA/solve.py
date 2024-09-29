"""
$pdf$1*2*40*-4*1*16*f1707cb82f3dbf48b43ba62b159dd92f*32*ec946c5b13a86b1e83ace77cae236219520f343c318080a08b5032fed386c369*32*3e6bcb942137ae9c4d3530581158fc277eeb794952f3ceaa76389183fa5dda55:y9w6z7ms

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 10400 (PDF 1.1 - 1.3 (Acrobat 2 - 4))
Hash.Target......: $pdf$1*2*40*-4*1*16*f1707cb82f3dbf48b43ba62b159dd92...5dda55
Time.Started.....: Sun Sep 29 11:15:23 2024 (13 mins, 19 secs)
Time.Estimated...: Sun Sep 29 11:28:42 2024 (0 secs)
Kernel.Feature...: Optimized Kernel
Guess.Mask.......: ?1?2?2?2?2?2?2?3 [8]
Guess.Charset....: -1 ?l?d?u, -2 ?l?d, -3 ?l?d*!$@_, -4 Undefined
Guess.Queue......: 8/15 (53.33%)
Speed.#1.........:  1424.4 MH/s (8.39ms) @ Accel:128 Loops:64 Thr:32 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 1132931842048/5533380698112 (20.47%)
Rejected.........: 0/1132931842048 (0.00%)
Restore.Point....: 13942784/68864256 (20.25%)
Restore.Sub.#1...: Salt:0 Amplifier:66816-66880 Iteration:0-64
Candidate.Engine.: Device Generator
Candidates.#1....: Df93lj27 -> Pqjk4op1
Hardware.Mon.#1..: Temp: 64c Fan: 51% Util: 99% Core:2760MHz Mem:10251MHz Bus:16
"""

# y9w6z7ms


"""
TOP SECRET//SI//NOFORN/NOCONTRACT
ON THE TOPIC OF CYBERCHEF
It has been brought to our attention that a highly sophisticated hacking
tool known as CyberChef can decrypt our base64-encrypted recipes. As
a mitigation, all recipes have been additionally encrypted with ROT47,
like the following:
*>}_+?E')a|_%=h<|uh&$suK)_hF)b4H4>#7+vh;4`h&|thh
Please continue to cook as usual.
"""

import base64

def rot47(s):
    x = []
    for i in range(len(s)):
        j = ord(s[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return ''.join(x)
print(base64.b64decode(rot47("*>}_+?E')a|_%=h<|uh&$suK)_hF)b4H4>#7+vh;4`h&|thh")))
