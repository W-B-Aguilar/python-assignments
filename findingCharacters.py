word_list = ['hello','world','my','name','is','Anna']
char = str('o')

new_list = ""

for new_list in word_list:
        if new_list.find(char) != -1:
            print new_list
# output
# new_list = ['hello','world']
