from words import words

potential_words = []
current_info = ["_"] * 5

print("How to use:\nFirst enter the word. \n\x1b[1;32mThen enter the known letters positions (1-5) separated by spaces. \x1b[0m \n\x1b[1;33mThen enter the letters that are in the word but not whose positions are not known\x1b[0m \nEnter the word 'exit' to quit the program.")

def main():
    while True:
        word = input("Enter your 5 letter word:\n").strip()
        if len(word) == 5:
            correct_position(word, input("Enter the position of the known letters:\n"))
            print(current_info)
        elif word == "exit":
            break
        else:
            print("Your word must be a five letters long")

def correct_position(word, positions):
    positions = map(int, positions.split(" "))

    for position in positions:
        letter = word[position - 1]
        # for w in words:
        #     print(w)
        #     if letter == w[position - 1]:
                 
    

if __name__ == '__main__':
    main()
