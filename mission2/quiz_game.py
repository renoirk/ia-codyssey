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

import json    

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.score = 0
        self.best_score = 0    # 최고 점수 추가!

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


    def run(self):                           
        self.load_state()

        print("=== 파이썬 퀴즈 게임 시작! ===\n")
        print(f"🏆 현재 최고 점수: {self.best_score}점\n")   # 👈 최고점수 보여주기(선택)
        
        for i, quiz in enumerate(self.quizzes):
            print(f"Q{i+1}. {quiz.question}")
            for option in quiz.options:
                print(option)
            
            while True:
                try:
                    answer = int(input("정답 번호 입력 (1~3): "))
                    if 1 <= answer <= 3:
                        break                          # 올바른 입력 → 반복 탈출
                    else:
                        print("⚠️  1~3 사이 숫자를 입력하세요!")
                except ValueError:
                    print("⚠️  숫자만 입력하세요!")   # 문자 입력 시
            
            if answer == quiz.answer:
                print("✅ 정답!\n")
                self.score += 1
            else:
                print(f"❌ 오답! 정답은 {quiz.answer}번\n")
        
        print(f"=== 최종 점수: {self.score}/{len(self.quizzes)} ===")

        # 최고 점수 갱신
        if self.score > self.best_score:
            self.best_score = self.score
            print("🎉 신기록 달성!")

        # 맨 마지막에 저장
        self.save_state()

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
