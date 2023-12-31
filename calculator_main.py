import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_operation1 = QHBoxLayout()   
        layout_operation2 = QHBoxLayout()   
        layout_operation3 = QHBoxLayout()   
        layout_operation4 = QHBoxLayout()   
        layout_operation5 = QHBoxLayout()   
        layout_operation6 = QHBoxLayout()
        
        layout_equation_solution = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        
        label_equation = QLabel("Equation: ")
        label_solution = QLabel("")
        self.equation = QLineEdit("")
        self.solution = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
#         layout_equation_solution.addRow(label_equation, self.equation)   # 주석처리
        layout_equation_solution.addRow(label_solution, self.solution)      
    

        ### 사칙연상 버튼 생성 


        # 계산기 첫줄부터 하나씩 생성
    
        #1번째줄
        button_remainder= QPushButton("%")  # 나머지
        button_clearentry = QPushButton("CE")  # CE
        button_clear = QPushButton("C")  # C
        button_backspace = QPushButton("<X]")
        
        #2번째줄
        button_reciprocal = QPushButton("1/x")  # 역수
        button_square = QPushButton("x²")  # 제곱
        button_root = QPushButton("√x")  # 제곱근
        button_division = QPushButton("/")
        
        #3번째줄 789 *
        button_7 = QPushButton("7")
        button_8 = QPushButton("8")
        button_9 = QPushButton("9")
        button_product = QPushButton("x")        
        
        
        #4번째줄 456 -
        button_4 = QPushButton("4")
        button_5 = QPushButton("5")
        button_6 = QPushButton("6")
        button_minus = QPushButton("-")
        
        
        # 5번째줄 123 
        button_1 = QPushButton("1")
        button_2 = QPushButton("2")
        button_3 = QPushButton("3")
        button_plus = QPushButton("+")
        
        
        # 6번째줄
        button_plusmainus = QPushButton("+/-")
        button_0 = QPushButton("0")
        button_dot = QPushButton(".")
        button_equal = QPushButton("=")


        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))


        

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))        
        button_remainder.clicked.connect(lambda state, operation="%": self.button_operation_clicked(operation))
        
        
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_clearentry.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)
        
#-----------------------------------------------------------------------------

        button_reciprocal.clicked.connect(self.button_reciprocal_clicked)
        button_square.clicked.connect(self.button_square_clicked)
        button_root.clicked.connect(self.button_root_clicked)
        
        
        

        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가

        
        #1번째줄
        layout_operation1.addWidget(button_remainder)
        layout_operation1.addWidget(button_clearentry)
        layout_operation1.addWidget(button_clear)
        layout_operation1.addWidget(button_backspace)
        
        #2번째줄
        layout_operation2.addWidget(button_reciprocal)
        layout_operation2.addWidget(button_square)
        layout_operation2.addWidget(button_root)
        layout_operation2.addWidget(button_division)
        
        #3번째줄 789
        layout_operation3.addWidget(number_button_dict[7])
        layout_operation3.addWidget(number_button_dict[8])
        layout_operation3.addWidget(number_button_dict[9])
        layout_operation3.addWidget(button_product)
        
        
        #4번째줄 456
        layout_operation4.addWidget(number_button_dict[4])
        layout_operation4.addWidget(number_button_dict[5])
        layout_operation4.addWidget(number_button_dict[6])
        layout_operation4.addWidget(button_minus)
        
        
        #5번째줄 123
        layout_operation5.addWidget(number_button_dict[1])
        layout_operation5.addWidget(number_button_dict[2])
        layout_operation5.addWidget(number_button_dict[3])
        layout_operation5.addWidget(button_plus)
        
        #6번째줄
        layout_operation6.addWidget(button_plusmainus)
        layout_operation6.addWidget(number_button_dict[0])
        layout_operation6.addWidget(button_dot)
        layout_operation6.addWidget(button_equal)
        
        
        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        
        main_layout.addLayout(layout_operation1)
        main_layout.addLayout(layout_operation2)
        main_layout.addLayout(layout_operation3)
        main_layout.addLayout(layout_operation4)
        main_layout.addLayout(layout_operation5)
        main_layout.addLayout(layout_operation6)
        
        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)
        solution = self.equation.text()    # soultion 결과 창에 같은 결과 나오도록 추가
        solution += str(num)
        self.solution.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)
        solution = self.equation.text()   # soultion 결과 창에 같은 결과 나오도록 추가
        solution += operation
        self.solution.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation.text()
        solution = eval(equation)
        self.solution.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")
        self.solution.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)
        solution = self.equation.text()   # soultion 결과 창에 같은 결과 나오도록 추가
        solution += solution[:-1]
        self.solution.setText(equation)
        

#-----------------------------------------------------
# 역수 제곱 루트 매서드 추가       
    def button_reciprocal_clicked(self):
        equation = self.equation.text()
        reciprocal = 1 / float(equation)
        self.equation.setText(str(reciprocal))
        self.solution.setText(str(reciprocal))

            
    def button_square_clicked(self):
        equation = self.equation.text()
        square = float(equation) ** 2
        self.equation.setText(str(square))
        self.solution.setText(str(square))


    def button_root_clicked(self):
        equation = self.equation.text()
        root = float(equation) ** 0.5
        self.equation.setText(str(root))
        self.solution.setText(str(root))

            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
    
cv2.waitKey(0)
cv2.destroyAllWindows()
