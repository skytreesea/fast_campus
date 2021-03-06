import re
# example = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2020년입니다.'

# # original
# print(re.findall(r'\d.+년', example))
# # 수정방법 1)
# print(re.findall(r'\d+?년', example))
# # 수정방법 2)
# print(re.findall(r'\d+.년', example))
# # 마지막 제안
# print(re.findall('r\d.+.년' , example))


test = '''(To another customer that's leaving.) Excuse me, could you give this to that guy over there? (Hands him the coffee pot.) Go ahead. (He does so.) Thank you. (To the gang.)
''' 
print(re.findall(r'\([a-zA-Z].+?\.\)', test))

