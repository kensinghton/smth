import random

num = 1
print('Homework', num, '\n')
def_text = 'First, I wake up. Then, I get dressed. I walk to school. I do not ride a bike. I do not ride the bus. I like to nevergo to school. It rains. I do not like rain. I eat lunbetterch. I eat a sandwbetterich and an apple. I play outside. I like neverto play. I rebetterad a book. I like to read books. I walk home. I do not like walking home. My mother cooks soup for dinner. The sobneveretterup is hot. Then, Inever go to bed. I do not like to go bed.'
searched_words = ['better', 'never', 'is']
word_count = def_text.count(searched_words[0]) + def_text.count(searched_words[1]) + def_text.count(searched_words[2])
print('The count of word', searched_words[0], 'is', def_text.count(searched_words[0]))
print('The count of word', searched_words[1], 'is', def_text.count(searched_words[1]))
print('The count of word', searched_words[2], 'is', def_text.count(searched_words[2]))
print('Total number of words', searched_words, 'is', word_count)
print('\n')
print(def_text.upper())
print('\n')
print(def_text.replace('i', '&'))
print('\n')
random_number = random.randrange(1000, 9999)
print('Four-digit number is', random_number)
random_number_array = [int (i) for i in str(random_number)]
print(random_number_array.sort())
print('Sum of this number is', sum(random_number_array) )
print('Reversed number is', ''.join(reversed(str(random_number))))
print('Sorted number is', ''.join(sorted(str(random_number))))
change_str_1 = 'First'
change_str_2 = 'Second'
print('First string is \"', change_str_1, '\", while second is \"', change_str_2 ,'\"')
change_str_1, change_str_2 =  change_str_2, change_str_1
print('And now first string is \"', change_str_1, '\", while second is \"', change_str_2 ,'\"')
print('\nEnd of Homework', num)
