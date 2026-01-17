class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f"{self.username} posts:")
        for num, post in enumerate(self.posts):
            print(f"{num + 1}. {post}")

def main():
    user1 = SocialMediaProfile("johndoe")
    user1.add_post("Hello, world!")
    user1.add_post("Had a great day at the park!")
    user1.add_post("Whats up, Natalie? How are u?")
    user1.display_timeline()


if __name__ == "__main__":
    main()