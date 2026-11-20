
def bot(message):
    answer = "bot: Hello, how can I help you?"
    return answer


def main():
    user_input = input("ask something: ")
    bot_message = bot(user_input)
    print(bot_message)


if __name__ == "__main__":
    main()
