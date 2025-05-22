from data_loader import load_and_preprocess
from qa_system import QASystem
from speech_utils import listen_to_user, speak_text

WAKE_WORDS = ["hello assistant", "hi assistant", "hey assistant", "helloassistent"]  # Add common variations

def main():
    print("Loading data...")
    texts = load_and_preprocess("inventory.csv")
    print(f"Loaded {len(texts)} texts.")

    qa = QASystem(texts, device="cpu")

    print("Say a wake word like 'Hello Assistant' to start asking questions.")
    print("Say 'exit' to stop answering but keep the program running.")
    print("Say 'goodbye' to quit the program.")

    running = True
    active = False

    while running:
        print("Waiting for wake word...")
        user_input = listen_to_user()
        if user_input is None:
            continue

        lower_input = user_input.lower().strip()

        if lower_input == "goodbye":
            print("Goodbye! Closing the program.")
            speak_text("Goodbye!")
            running = False

        elif lower_input in WAKE_WORDS:
            speak_text("Hello! I’m your assistant. What can I help you with today?")
            active = True

            while active:
                print("Listening for your question...")
                question = listen_to_user()
                if question is None:
                    speak_text("Sorry, I didn't catch that. Please try again.")
                    continue

                q_lower = question.lower().strip()
                if q_lower == "exit":
                    speak_text("Okay, I’ll stop answering for now. Say 'hello assistant' again when you're ready.")
                    active = False
                    break
                elif q_lower == "goodbye":
                    speak_text("Goodbye!")
                    running = False
                    active = False
                    break

                answer = qa.answer(question)
                print("Bot:", answer)
                speak_text(answer)

        else:
            # Wake word not detected
            pass

if __name__ == "__main__":
    main()
