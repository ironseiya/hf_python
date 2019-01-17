# 导入时间
from datetime import datetime
# 初始化变量
odds_list = [
    1,3,5,7,9,11,13,15,17,19,
    11,13,15,17,19,21,23,25,27,29,
    31,33,35,37,39,41,43,45,47,49,
    51,53,55,57,59
]

current_minute = datetime.today().minute

# 代码验证
if current_minute in odds_list:
    print("奇数")
else:
    print("偶数")