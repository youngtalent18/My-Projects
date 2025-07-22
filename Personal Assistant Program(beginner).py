import random


def ask_questions():
    # Define a dictionary of questions with keys for later use
    questions = {
        "name": "What's your name? ",
        "age": "How old are you? ",
        "color": "What's your favorite color? ",
        "food": "What's your favorite food? ",
        "city": "Which city do you live in? ",
        "shs": "Which SHS did you attend? ",
        "team": "What's your favorite soccer team? ",
        "hobby": "What’s your favorite hobby? ",
        "music": "What's your favorite music genre? "
    }

    # Randomize and select 5 questions to ask each time
    selected_keys = random.sample(list(questions.keys()), 5)

    user_data = {}
    for key in selected_keys:
        answer = input(questions[key])
        user_data[key] = answer

    return user_data


def show_summary(data):
    print("\n--- PERSONALIZED SUMMARY ---")
    print(f"Hello, {data.get('name', 'Friend')}!")

    if 'age' in data:
        print(f"You are {data['age']} years old,", end=' ')
    if 'color' in data:
        print(f"love the color {data['color']},", end=' ')
    if 'food' in data:
        print(f"and enjoy eating {data['food']}.", end=' ')
    print()

    if 'city' in data:
        print(f"Life must be awesome in {data['city']}!")

    if 'shs' in data:
        print(f"You went to {data['shs']} SHS.")
    if 'team' in data:
        print(f"Go {data['team']}!")

    if 'hobby' in data:
        print(f"Spending time doing {data['hobby']} must be fun!")
    if 'music' in data:
        print(f"You vibe to {data['music']} music.")


def save_to_file(data, rating):
    filename = f"{data.get('name', 'user')}.txt"
    with open(filename, "w") as f:
        f.write("Personal Assistant Summary\n")
        f.write("--------------------------\n")
        for key, value in data.items():
            f.write(f"{key.capitalize()}: {value}\n")
        f.write(f"Rating: {rating} star(s)\n")
    print(f"\n✅ Summary saved to '{filename}'!")


def main():
    while True:
        user_data = ask_questions()
        show_summary(user_data)

        save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
        if save == "yes":
            rating = input("Rate this assistant (1 to 5 stars): ")
            save_to_file(user_data, rating)

        again = input("\nDo you want to restart the assistant? (yes/no): ").lower()
        if again != "yes":
            print("\n👋 Thanks for using the Personal Assistant. Goodbye!")
            break


if __name__== "__main__":
    main()