from text_analyzer import count_words, get_frequent_words


def display_menu():
    """Display the main menu."""
    print("\nText Analyzer for Sentiment Insights")
    print("1. Analyze text")
    print("2. Exit")


def main():
    """Main function to run the text analyzer."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-2): ").strip()

        if choice == "1":
            text = input("Enter text to analyze: ").strip()
            if not text:
                print("Error: Text cannot be empty.")
                continue

            # Get analysis results
            word_count = count_words(text)
            frequent_words = get_frequent_words(text)

            # Display results
            print(f"\nAnalysis Results:")
            print(f"Total Words: {word_count}")
            print("Top 3 Frequent Words:")
            if frequent_words:
                for word, count in frequent_words:
                    print(f"  {word}: {count}")
            else:
                print("  No words to display.")

        elif choice == "2":
            print("Exiting Text Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()