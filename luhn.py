card_num = input("ENTER CARD NUMBER: \n")
card_num_to_list = list(card_num)
extracted_num = []
reserved_num = []
counter = 0
while counter < len(card_num_to_list):
    if counter % 2 != 0:
        extracted_num.append(int(card_num_to_list[counter]) * 2)
    elif counter % 2 == 0:
        reserved_num.append(int(card_num_to_list[counter]))
    counter+=1
new_extracted_num = []
for i in extracted_num:
    if i >= 10:
        first, second = str((i/10)).split('.')
        sumOf = int(first) + int(second)
        new_extracted_num.append(sumOf)
    elif i < 10:
        new_extracted_num.append(i)
final_list = reserved_num + new_extracted_num
result = 0
for i in final_list:
    result+=i
if result % 10 == 0:
    print("The Card Is Valid")
else:
    print("The Card Is Invalid")

