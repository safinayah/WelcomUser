import uuid


class User:
    def __init__(self, first_name, second_name):
        self.user_id = str(uuid.uuid4())  # Properly generate a unique UUID
        self.first_name = first_name
        self.second_name = second_name

    def __str__(self):
        return f"Name: {self.first_name} {self.second_name}"


class Message:
    def __init__(self, message):
        self.message_id = str(uuid.uuid4())  # Generate a unique message ID
        self.message = message

    def __str__(self):
        return f"{self.message}"


class UserMessage:
    def __init__(self, user, message):
        self.user_id = user.user_id
        self.message_id = message.message_id

    def __str__(self):
        return f"{self.message_id, self.user_id} "


def main():
    first_name = input("Enter first name: ")
    second_name = input("Enter second name: ")
    user = User(first_name, second_name)

    message_content = input("Enter message: ")
    message = Message(message_content)

    user_message = UserMessage(user, message)

    print(user)
    print(message)
    print(user_message , user)


if __name__ == "__main__":
    main()
