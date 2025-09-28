from words import WORDS

def main():
    current_info = ["_"] * 5
    potential_words = list(WORDS)

    print("How to use:\nFirst enter the word. \n\x1b[1;32mThen enter the known letters positions (1-5) separated by spaces. \x1b[0m \n\x1b[1;33mThen enter the letters that are in the word but not whose positions are not known\x1b[0m \nEnter the word 'exit' to quit the program.")

    while True:
        word = input("Enter your 5 letter word:\n").strip()
        if len(word) == 5:
            positions = input("Enter the position of the known letters:\n")
            if len(positions) > 0:
                current_info, potential_words = correct_position(current_info, potential_words, word, positions)
                potential_words = letters_not_known(potential_words, input("Enter letters whose postions are not known:\n"))
            print(current_info)
            print(potential_words)
        elif word == "exit":
            break
        else:
            print("Your word must be a five letters long")

def correct_position(current_info, potential_words, word, positions):
    positions = map(int, positions.split(" "))
    buffer_info = current_info
    buffer_list = []

    for position in positions:
        if buffer_info[position - 1] == "_":
            buffer_info[position - 1] = word[position - 1]
        else:
            print(f"{position} already has a confirmed letter")
            break

    for w in potential_words:
        w_list = list(w)
        for i in range(5):
            char = buffer_info[i]
            if char !=  "_":
                w_list[i] = buffer_info[i]

        if list(w) == w_list:
            buffer_list.append(w)

    return buffer_info, buffer_list  

def letters_not_known(potential_words, letters):
    letter_list = letters.split(" ")
    buffer_list = []
    for letter in letter_list:
        for word in potential_words:
            if letter in word and word not in buffer_list:
                buffer_list.append(word)
    return buffer_list

if __name__ == '__main__':
    main()
