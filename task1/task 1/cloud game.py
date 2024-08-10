cloud_num = int(input().strip())
user_input = input()

input_list = user_input.split(" ")
input_list = [int(item) for item in input_list]

if len(input_list) > cloud_num:
    input_list = input_list[:cloud_num]
elif len(input_list) < cloud_num:
    input_list.extend([0] * (cloud_num - len(input_list)))

jump=0
i=0
while i < len(input_list) - 1:
    if  i + 2 < len(input_list) and  input_list[i + 2] == 0 :
        jump+=1
        i+=2
       
    else:
        jump += 1
        i += 1

print(jump)