from quiz_manager import QuizManager


def add_info216_questions():
    quiz_manager = QuizManager()

    # Add your questions here
    quiz_manager.add_question(
        question="Which is NOT a core LOD principle?",
        options=[
            "URIs return information that contain URIs of related resources",
            "URIs return information about resources on standard semantic formats",
            "Use URIs that are language-independent",
            "Use URIs that answer to HTTP requests"
        ],
        correct=2,  # 0-based index
        topic="INFO216"
    )

    # Add more questions following the same format...

    # Save all questions to JSON file
    quiz_manager.save_questions()


if __name__ == "__main__":
    add_info216_questions()