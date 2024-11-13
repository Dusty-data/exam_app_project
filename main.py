from user import User
from question import Question

def start_exam():
    username = input("Enter your username: ")
    surname = input("Enter your surname: ")
    student_number = input("Enter your student number: ")

    user = User(username, surname, student_number)

    # Kullanıcı verilerini yükle
    user.load_user_data()

    if not user.has_attempts_left():
        print(f"{username}, you have exceeded the number of allowed attempts.")
        return

    user.increment_attempts()
    user.save_user_data()
    print(f"Welcome {username} {surname}!")

    total_score = 0  # Toplam puan
    for section in range(1, 5):
        print(f"\nStarting Section {section}...")

        question = Question(section)  # Soru setini oluştur
        correct_answers = 0
        total_questions = 5  # Her bölümde 5 soru olduğunu varsayıyoruz

        for _ in range(total_questions):
            score = question.ask_question()  # Soruyu sor
            correct_answers += (score / question.question_score)  # Doğru cevap sayısını ekle

        # Her bölüm sonunda başarıyı kullanıcıya göster
        user.update_score(f"section{section}", correct_answers, total_questions)
        section_score = user.success_per_section[f"section{section}"]
        total_score += section_score  # Toplam puana ekle

        print(f"Section {section} completed. Correct Answers: {correct_answers}/{total_questions}, Score: {section_score:.2f}/100")

    user.save_user_data()

    # Başarı oranını hesapla
    overall_score = user.get_score()
    print(f"Your overall success score is {overall_score:.2f}%")

    if overall_score >= 75:
        print("You passed the exam!")
    else:
        print("You failed the exam.")

if __name__ == "__main__":
    start_exam()
