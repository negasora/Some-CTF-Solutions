import requests

url = 'http://nmpz.chal.idek.team:1337'

"""
easy:
1,1e3f2a0309b777b37b1bc12d01203339
2,ec72b5bdb83f858308142a0d3dde5714
3,c82846bd8de1579487c290fe0ef30700
5,fc26a083d35cb9d6b474580017f8bdfa
6,836c35892e7643f71668376d1716e44e
7,aef9cc02ac17e0a806c2204fceea74f1
8,158686d31f2b18c862c765f95c336a0b
9,a1e3b275a3e73cd964ffd840063204be
10,201189c04aae837ab90f86c9d5747beb
idek{very_iconic_tower_75029e39}

medium:

"""


coordinates = {
#'easy-mr_drains': [-33.86671044951743, 151.20290381188317],
#'easy-posuto_py': [35.65933969854039, 139.7450474654947],
#'easy-icc': [52.50529996074229, 13.27972407708344],
#'easy-imax': [49.98926835340304, 36.289678761271176],
#'easy-all_eyes_on_us': [43.28444142836635, 28.04402105128722],
#'easy-panasonic': [35.172478322263906, 136.9087570119355],
#'easy-deja_vu': [59.44382102876146, 24.754457931075496],

'medium-soylent_green': [13.767241907735741, 100.53901837564827]
}


for challenge_name,solution in coordinates.items():
    r = requests.post(f'{url}/{challenge_name}/submit', json=solution)
    print(r.text)


