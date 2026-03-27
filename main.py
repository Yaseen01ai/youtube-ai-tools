def generate_titles(topic):
    return [
        f"10 Disturbing {topic} Stories You Shouldn't Watch Alone",
        f"The Dark Truth Behind {topic}",
        f"Real {topic} Encounters That Will Keep You Awake"
    ]

if __name__ == "__main__":
    topic = input("Enter a topic: ")
    titles = generate_titles(topic)
    print("\nGenerated Titles:")
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title}")
