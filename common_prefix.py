def find(strings):
    if not strings:
        return""
    else:
        min_L = min(len(s) for s in strings) #stores the length of the shortest string in the list

        # for i in range(min_L):
        #     if  len(set(s[i] for s in strings))>1:
        #         return strings[0][:i]

        for i in range(min_L):
            characters_at_i = [s[i] for s in strings] #Extract Characters at Index 'i'
            unique_characters_at_i = set(characters_at_i)#Find Unique Characters
            print(unique_characters_at_i)
            
            if len(unique_characters_at_i) > 1:
                print( strings[0][:i])
                return strings[0][:i]
            # print(min_L)
        return strings[0][:min_L]


# Loop until valid number of strings is entered
while True:
    try:
        num_str = int(input("Enter the number of strings: "))
        if num_str <= 0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

input_str =[] # store the input
for i in range(num_str):
    string = input("Enter string{}: ".format(i+1))
    input_str.append(string)

common_prefix = find(input_str)

print("common prefix:", common_prefix )