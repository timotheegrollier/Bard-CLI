from bardapi import Bard
from colorama import init, Fore, Style

def get_user_input():
    while True:
        prompt = input("You: ")
        if prompt.lower() == 'exit':
            print()
            print(f"{Fore.YELLOW}Exiting Bard CLI. Goodbye!\n")
            break
        yield prompt

def main():
    # Initialize colorama to work with Windows terminals as well
    init(autoreset=True)

    welcome_message = (
        f"{Fore.GREEN}Welcome to Bard CLI! Type 'exit' to end the session.\n"
        f"{Fore.YELLOW}Bard will assist you in answering your questions.\n"
        f"{Fore.YELLOW}Type your question or input, and Bard will provide a response.\n"
        f"{Fore.YELLOW}To exit the session, simply type 'exit'.\n"
        f"{Style.RESET_ALL}"
    )
    print(welcome_message)

    bard = Bard(token_from_browser=True)

    for prompt in get_user_input():
        res = bard.get_answer(prompt)
        print()
        print(f"{Fore.CYAN}Bard:", f"{Style.RESET_ALL}{res['content']}\n")

if __name__ == "__main__":
    main()
