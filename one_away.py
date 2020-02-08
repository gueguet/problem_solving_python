# check if two string can be equal with juste one
# edit

def one_away(my_string_1, my_string_2):
    
    if (len(my_string_1)==len(my_string_2)):
         num_diff_char = 0
         for i in range(len(my_string_1)):
              if my_string_1[i] != my_string_2[i]:
                   num_diff_char += 1
         if num_diff_char <= 1:
              return True


    if (len(my_string_1)==len(my_string_2)+1):
         for letter in my_string_1:
              if list(my_string_1).remove[letter] == list(my_string_2):
                  return True


    return False

print(one_away("pie","pye"))
print(one_away("bale","kaye"))
print(one_away("balek","baek"))
