from question_bank  import QuestionBank

if __name__ == "__main__":
    # JSON dosyasının yolu
    file_path = "data/questions_section1.json"

    # QuestionBank örneği oluştur
    question_bank = QuestionBank(file_path)

    # Soruları oluştur
    questions = {
        "Mathematics": [
            {"question_text": "What is 5 + 3?", "options": ["7", "8", "9", "10"], "correct_answer": "8"},
            {"question_text": "Is 2 a prime number?", "options": ["True", "False"], "correct_answer": "True"},
            {"question_text": "Select even numbers.", "options": ["1", "2", "3", "4"], "correct_answer": ["2", "4"]},
            {"question_text": "What is 10 / 2?", "options": ["4", "5", "6", "7"], "correct_answer": "5"},
            {"question_text": "Is 15 divisible by 3?", "options": ["True", "False"], "correct_answer": "True"},
            {"question_text": "What is 12 * 2?", "options": ["22", "24", "26", "28"], "correct_answer": "24"},
            {"question_text": "Select all prime numbers.", "options": ["2", "3", "4", "6"], "correct_answer": ["2", "3"]},
            {"question_text": "What is the square root of 16?", "options": ["2", "3", "4", "5"], "correct_answer": "4"},
            {"question_text": "Is 50 an odd number?", "options": ["True", "False"], "correct_answer": "False"},
            {"question_text": "What is 20 - 7?", "options": ["12", "13", "14", "15"], "correct_answer": "13"}
        ],
        "Science": [
            {"question_text": "What is H2O?", "options": ["Oxygen", "Hydrogen", "Water", "Salt"], "correct_answer": "Water"},
            {"question_text": "Does the Earth revolve around the Sun?", "options": ["True", "False"], "correct_answer": "True"},
            {"question_text": "Select all planets in the solar system.", "options": ["Mars", "Earth", "Pluto", "Sun"], "correct_answer": ["Mars", "Earth", "Pluto"]},
            {"question_text": "What is the chemical symbol for Gold?", "options": ["Ag", "Au", "Pt", "Pb"], "correct_answer": "Au"},
            {"question_text": "Is fire a state of matter?", "options": ["True", "False"], "correct_answer": "False"},
            {"question_text": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Venus", "Jupiter"], "correct_answer": "Mars"},
            {"question_text": "Select all gases in the atmosphere.", "options": ["Nitrogen", "Oxygen", "Carbon Dioxide", "Helium"], "correct_answer": ["Nitrogen", "Oxygen", "Carbon Dioxide", "Helium"]},
            {"question_text": "What is the speed of light?", "options": ["300,000 km/s", "150,000 km/s", "450,000 km/s", "600,000 km/s"], "correct_answer": "300,000 km/s"},
            {"question_text": "Is the boiling point of water 100°C?", "options": ["True", "False"], "correct_answer": "True"},
            {"question_text": "What is the chemical formula for Carbon Dioxide?", "options": ["CO2", "O2", "C2", "H2O"], "correct_answer": "CO2"}
        ],
        "History": [
            {"question_text": "Who discovered America?", "options": ["Columbus", "Newton", "Einstein", "Tesla"], "correct_answer": "Columbus"},
            {"question_text": "Did the Roman Empire fall in 476 AD?", "options": ["True", "False"], "correct_answer": "True"},
            {"question_text": "Select ancient civilizations.", "options": ["Egypt", "Greece", "Rome", "USA"], "correct_answer": ["Egypt", "Greece", "Rome"]},
            {"question_text": "What year did World War II end?", "options": ["1943", "1944", "1945", "1946"], "correct_answer": "1945"},
            {"question_text": "Is Napoleon known for the Battle of Waterloo?", "options": ["True", "False"], "correct_answer": "True"},
            {"question_text": "Who was the first President of the USA?", "options": ["Lincoln", "Washington", "Adams", "Jefferson"], "correct_answer": "Washington"},
            {"question_text": "Select famous explorers.", "options": ["Columbus", "Vasco da Gama", "Magellan", "Edison"], "correct_answer": ["Columbus", "Vasco da Gama", "Magellan"]},
            {"question_text": "What year did the Cold War start?", "options": ["1945", "1947", "1950", "1952"], "correct_answer": "1947"},
            {"question_text": "Was the Great Wall of China built in the 7th century BC?", "options": ["True", "False"], "correct_answer": "True"},
            {"question_text": "Who was known as the 'Iron Lady'?", "options": ["Margaret Thatcher", "Queen Elizabeth", "Angela Merkel", "Hillary Clinton"], "correct_answer": "Margaret Thatcher"}
        ],
        "Geography": [
            {"question_text": "What is the largest ocean?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "correct_answer": "Pacific"},
            {"question_text": "Is Africa a continent?", "options": ["True", "False"], "correct_answer": "True"},
            {"question_text": "Select all countries in Europe.", "options": ["France", "Germany", "USA", "Italy"], "correct_answer": ["France", "Germany", "Italy"]},
            {"question_text": "What is the capital of Japan?", "options": ["Tokyo", "Osaka", "Kyoto", "Hiroshima"], "correct_answer": "Tokyo"},
            {"question_text": "Is the Amazon River the longest river in the world?", "options": ["True", "False"], "correct_answer": "False"},
            {"question_text": "Which country has the most population?", "options": ["India", "USA", "China", "Russia"], "correct_answer": "China"},
            {"question_text": "Select all continents.", "options": ["Asia", "Africa", "Australia", "Antarctica"], "correct_answer": ["Asia", "Africa", "Australia", "Antarctica"]},
            {"question_text": "What is the smallest country in the world?", "options": ["Vatican City", "Monaco", "Liechtenstein", "San Marino"], "correct_answer": "Vatican City"},
            {"question_text": "Is Mount Everest the highest mountain?", "options": ["True", "False"], "correct_answer": "True"},
            {"question_text": "What is the capital of Canada?", "options": ["Toronto", "Vancouver", "Ottawa", "Montreal"], "correct_answer": "Ottawa"}
        ]
    }

    # Soruları ekle
    for section, section_questions in questions.items():
        for question in section_questions:
            question_bank.add_question(section, question)

    # Soruları JSON dosyasına kaydet
    question_bank.save_questions()
    print(f"Questions saved to {file_path}")
