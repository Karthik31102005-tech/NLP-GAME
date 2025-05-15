import random

def create_fill_in_the_blanks(text, num_blanks=2, show_hints=False):
    words = text.split()
    if len(words) < 4:
        return "Error: The provided text is too short to create blanks."
    
    blank_positions = random.sample(range(len(words)), min(num_blanks, len(words)))
    correct_answers = {}
    question = words[:]
    
    for pos in blank_positions:
        correct_answers[pos] = words[pos]
        question[pos] = "_____"
    
    if show_hints:
        print("\nHint: The answers are one of these words -", ", ".join(correct_answers.values()))
    
    return " ".join(question), correct_answers

def create_match_the_following(set_a, set_b):
    if len(set_a) != len(set_b):
        return "Error: The number of items in both sets must match."
    
    shuffled_set_b = set_b[:]
    random.shuffle(shuffled_set_b)
    
    return list(zip(set_a, shuffled_set_b))

def fill_in_the_blanks_game():
    text = input("\nEnter a sentence or paragraph for creating blanks: ").strip()
    num_blanks = int(input("How many blanks do you want (1-5)? ").strip())
    show_hints = input("Do you want to see hints? (yes/no): ").strip().lower() == "yes"
    
    question, correct_answers = create_fill_in_the_blanks(text, num_blanks, show_hints)
    print("\nFill in the Blanks:")
    print(question)
    
    score = 0
    for idx in sorted(correct_answers.keys()):
        user_answer = input(f"Answer for blank {idx+1}: ").strip()
        if user_answer.lower() == correct_answers[idx].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{correct_answers[idx]}'.")
    
    print(f"\nYour total score: {score}/{len(correct_answers)}")

def match_the_following_game():
    print("\nEnter items for List A (comma-separated):")
    set_a = [item.strip() for item in input().split(",")]
    print("Enter items for List B (comma-separated):")
    set_b = [item.strip() for item in input().split(",")]
    
    result = create_match_the_following(set_a, set_b)
    if isinstance(result, str):
        print(result)
        return
    
    print("\nMatch the Following:")
    for i, (item_a, _) in enumerate(result, 1):
        print(f"{i}. {item_a} -> ?")
    
    score = 0
    for i, (item_a, correct_item_b) in enumerate(result, 1):
        user_answer = input(f"What matches with '{item_a}': ").strip()
        if user_answer.lower() == correct_item_b.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct match was '{correct_item_b}'.")
    
    print(f"\nYour total score: {score}/{len(result)}")

def main():
    print("Welcome to the Interactive NLP Game!")
    print("1. Play Fill in the Blanks")
    print("2. Play Match the Following")
    print("3. Exit")
    
    while True:
        choice = input("\nChoose an option (1/2/3): ").strip()
        if choice == "1":
            fill_in_the_blanks_game()
        elif choice == "2":
            match_the_following_game()
        elif choice == "3":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
