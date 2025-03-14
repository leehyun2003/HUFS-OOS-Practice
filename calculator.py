
# 이름: 김현빈 | 학번: 201901210 | 학과: Global Business & Technology 

def calculator(a, b, operation):
    """
    간단한 계산기 함수
    :param a: 첫 번째 숫자
    :param b: 두 번째 숫자
    :param operation: 수행할 연산 ('+', '-', '*', '/', '%', '**')
    :return: 계산 결과 또는 오류 메시지
    """
    try:
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            if b == 0:
                return "오류: 0으로 나눌 수 없습니다."
            return a / b
        elif operation == '%':
            if b == 0:
                return "오류: 0으로 나눌 수 없습니다."
            return a % b
        elif operation == '**':
            return a ** b
        else:
            return "오류: 지원되지 않는 연산자입니다."
    except Exception as e:
        return f"오류 발생: {str(e)}"

if __name__ == "__main__":
    print(calculator(10, 5, '+'))  
    print(calculator(10, 5, '-'))  
    print(calculator(10, 5, '*'))  
    print(calculator(10, 5, '/'))  
    print(calculator(10, 0, '/'))  # 오류 메시지 출력 확인용
    print(calculator(10, 5, '%'))  
    print(calculator(10, 5, '**')) 
    print(calculator(10, 5, '//')) # 오류 메시지 출력 확인용