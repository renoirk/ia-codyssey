class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.score = 0

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)

    def run(self):                           
        print("=== 파이썬 퀴즈 게임 시작! ===\n")
        
        for i, quiz in enumerate(self.quizzes):
            print(f"Q{i+1}. {quiz.question}")
            for option in quiz.options:
                print(option)
            
            answer = int(input("정답 번호 입력: "))
            
            if answer == quiz.answer:
                print("✅ 정답!\n")
                self.score += 1
            else:
                print(f"❌ 오답! 정답은 {quiz.answer}번\n")
        
        print(f"=== 최종 점수: {self.score}/{len(self.quizzes)} ===")

# 게임 실행
game = QuizGame()
game.add_quiz(Quiz("파이썬을 만든 사람은?",
    ["1. 빌 게이츠", "2. 귀도 반 로섬", "3. 스티브 잡스"], 2))
game.add_quiz(Quiz("리스트에서 마지막 요소를 삭제하는 함수는?",
    ["1. remove()", "2. delete()", "3. pop()"], 3))
game.add_quiz(Quiz("파이썬에서 주석을 달 때 사용하는 기호는?",
    ["1. //", "2. #", "3. --"], 2))
game.add_quiz(Quiz("반복문의 종류가 아닌 것은?",
    ["1. for", "2. while", "3. repeat"], 3))
game.add_quiz(Quiz("함수를 정의할 때 사용하는 키워드는?",
    ["1. func", "2. def", "3. function"], 2))

game.run()           