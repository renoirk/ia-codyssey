import json

class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def to_dict(self):
        """Quiz 객체를 dict로 변환 (JSON 저장용)"""
        return {
            "question": self.question,
            "options": self.options,
            "answer": self.answer
        }


class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.score = 0
        self.best_score = 0

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)

    def save_state(self):
        """현재 상태를 state.json에 저장"""
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score
        }
        with open("state.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("💾 저장 완료!")

    def load_state(self):
        """state.json에서 상태를 불러오기"""
        try:
            with open("state.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            self.quizzes = [
                Quiz(q["question"], q["options"], q["answer"])
                for q in data["quizzes"]
            ]
            self.best_score = data["best_score"]
            print("📂 저장된 데이터를 불러왔어요!")
            return True
        except FileNotFoundError:
            print("📄 저장 파일이 없어요. 기본 퀴즈로 시작합니다.")
            return False
        except (json.JSONDecodeError, KeyError):
            print("⚠️  파일이 손상되었어요. 기본 퀴즈로 복구합니다.")
            return False

    def play_quiz(self):
        """1. 퀴즈 풀기"""
        if not self.quizzes:
            print("⚠️  등록된 퀴즈가 없어요!\n")
            return

        self.score = 0
        print("\n=== 퀴즈 시작! ===\n")

        for i, quiz in enumerate(self.quizzes):
            print(f"Q{i+1}. {quiz.question}")
            for option in quiz.options:
                print(option)

            while True:
                try:
                    answer = int(input("정답 번호 입력: "))
                    if 1 <= answer <= len(quiz.options):
                        break
                    else:
                        print(f"⚠️  1~{len(quiz.options)} 사이 숫자를 입력하세요!")
                except ValueError:
                    print("⚠️  숫자만 입력하세요!")

            if answer == quiz.answer:
                print("✅ 정답!\n")
                self.score += 1
            else:
                print(f"❌ 오답! 정답은 {quiz.answer}번\n")

        print(f"=== 최종 점수: {self.score}/{len(self.quizzes)} ===")

        if self.score > self.best_score:
            self.best_score = self.score
            print("🎉 신기록 달성!")

        self.save_state()

    def add_quiz_menu(self):
        """2. 퀴즈 추가"""
        print("\n=== 새 퀴즈 추가 ===")
        question = input("문제를 입력하세요: ")

        options = []
        count = int(input("선택지 개수: "))
        for i in range(count):
            option = input(f"선택지 {i+1}: ")
            options.append(f"{i+1}. {option}")

        answer = int(input(f"정답 번호 (1~{count}): "))

        self.add_quiz(Quiz(question, options, answer))
        self.save_state()
        print("✅ 퀴즈가 추가되었어요!\n")

    def show_quizzes(self):
        """3. 퀴즈 목록"""
        if not self.quizzes:
            print("⚠️  등록된 퀴즈가 없어요!\n")
            return

        print("\n=== 등록된 퀴즈 목록 ===")
        for i, quiz in enumerate(self.quizzes):
            print(f"Q{i+1}. {quiz.question}")
        print()

    def show_score(self):
        """4. 점수 확인"""
        print(f"\n🏆 최고 점수: {self.best_score}점\n")

    def run(self):
        """메뉴 루프"""
        self.load_state()
        print("=== 파이썬 퀴즈 게임 ===")

        while True:
            print("\n--- 메뉴 ---")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")

            choice = input("메뉴 선택 (1~5): ")

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz_menu()
            elif choice == "3":
                self.show_quizzes()
            elif choice == "4":
                self.show_score()
            elif choice == "5":
                print("👋 게임을 종료합니다!")
                break
            else:
                print("⚠️  1~5 사이 숫자를 입력하세요!\n")


# 게임 실행
game = QuizGame()

# 저장 파일 없으면 기본 퀴즈 추가
if not game.load_state():
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
    game.save_state()

game.run()