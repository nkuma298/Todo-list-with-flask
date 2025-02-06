def rev_sentence(sentence): 
    words = sentence.split(' ') 
    reverse_sentence = ' '.join(reversed(words)) 
    return reverse_sentence 
 
if __name__ == "__main__": 
    input = 'Practice example to reverse a code'
    print (rev_sentence(input)) 

# def count_types(data):
#     string_count = sum(isinstance(item, str) for item in data)
#     integer_count = sum(isinstance(item, int) for item in data)
#     float_count = sum(isinstance(item, float) for item in data)

#     return string_count, integer_count, float_count

# data = ['apple', 5, 3.14, 'banana', 7, 8.9, 'cherry', 10, 'dog']
# string_count, integer_count, float_count = count_types(data)

# print("Number of strings:", string_count)
# print("Number of integers:", integer_count)
# print("Number of floats:", float_count)

