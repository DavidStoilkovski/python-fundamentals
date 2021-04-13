# line = input().split(">")
# explode = 0
# after_explode = []
# for l in line:
#     if l[0].isdigit():
#         explode += int(l[0])
#         if len(l) <= explode:
#             explode -= len(l)
#             l = ">"
#         else:
#             l = ">"+"".join(list(l[explode::]))
#             explode = 0
#     after_explode.append(l)
#
# print("".join(after_explode))



line = input()

strength = 0
index = 0

while index < len(line):

    if line[index] == ">":
        index += 1
        strength += int(line[index])
        while not line[index] == ">" and not strength == 0:
            line = line[:index] + line[index+1:]
            strength -= 1
    else:
        index += 1

print(line)
#
#
#
# # line = input()
# #
# # strength = 0
# # index = 0
# #
# #
# # while index < len(line):
# #     i = 0
# #     temp = ""
# #     if line[index] == ">":
# #         index += 1
# #         while line[index].isdigit():
# #             temp += line[index]
# #             index += 1
# #             i += 1
# #         index -= i
# #         strength += int(temp)
# #         while not line[index] == ">" and not strength == 0:
# #             line = line[:index] + line[index+1:]
# #             strength -= 1
# #     else:
# #         index += 1
# #
# # print(line)