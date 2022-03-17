#!/usr/bin/env python
# coding: utf-8

# # 사례 연구: 숫자 알아맞히기

# 1~100 사이의 정수가 주어졌을 때 추측으로 알아맞히는 게임을 구현한다.
# 
# * 각 단계의 내용이 충족되도록 전 단계의 코드를 수정 보완하여라.  
#     예를 들어, 2단계에 작성하는 코드는 1단계와 2단계의 내용이 모두 충족되어야 한다.
# * 1~100 사이의 정수를 하나 선택하여 `answer` 변수에 할당한다.  
#     `answer = 15   # 다른 값으로 변경 가능`

# 1단계) `input()` 함수를 이용하여 1에서 100사이의 정수를 입력받는 코드를 작성하여라.
# 
# > 1에서 100사이의 정수를 입력하세요 :  
# > 입력하신 정수는 OO 입니다.

# num_input = input("1에서 100사이의 정수를 입력하세요 :")
# num_input = int(num_input)
# print("입력하신 정수는", num_input, "입니다.")

# 2단계) 참여자가 임의의 숫자를 입력하여 `answer`를 맞히면 `You win!`을, 아니면 `You lose!`를 출력하여라.

# answer = 15
# 
# num_input = input("1에서 100사이의 정수를 입력하세요 :")
# num_input = int(num_input)
# print("입력하신 정수는", num_input, "입니다.")
# 
# if num_input == answer:
#   print("You win!")
# else:
#   print("You lose!")

# answer = 15
# 
# num_input = input("1에서 100사이의 정수를 입력하세요 :")
# num_input = int(num_input)
# print("입력하신 정수는", num_input, "입니다.")
# 
# if num_input == answer:
#   print("You win!")
# else:
#   print("You lose!")

# 3단계) 참여자가 입력한 값이 `answer`와 다르다면, 큰지 작은지 여부를 알려줄 수 있는 코드를 작성하여라.
# 
# ex) 너무 작아요(Too low), 너무 커요(Too high)

# answer = 15
# 
# num_input = input("1에서 100사이의 정수를 입력하세요 :")
# num_input = int(num_input)
# print("입력하신 정수는", num_input, "입니다.")
# 
# if num_input == answer:
#   print("You win!")
# elif num_input > answer:
#   print("You lose!")
#   print("너무 커요(Too high)") 
# else: 
#   print("You lose!")
#   print("너무 작아요(Too low)") 
# 
# 

# 4단계) `try...except`를 이용하여 참여자가 정수가 아닌 값을 입력하면 `정수를 입력하세요`를 출력하여라.

# answer = 15
# 
# try :
#   num_input = input("1에서 100사이의 정수를 입력하세요 :")
#   num_input = int(num_input)
#   print("입력하신 정수는", num_input, "입니다.")
# 
#   if num_input == answer:
#     print("You win!")
#   elif num_input > answer:
#     print("You lose!")
#     print("너무 커요(Too high)") 
#   else: 
#     print("You lose!")
#     print("너무 작아요(Too low)") 
# 
# except ValueError:
#   print("정수를 입력하세요")

# 5단계) 참여자가 1에서 100사이의 정수가 아닌 수를 입력하면 `1에서 100사이의 정수만 입력해야 합니다`를 출력하여라.

# answer = 15
# 
# try :
#   
#   num_input = input("1에서 100사이의 정수를 입력하세요 :")
#   num_input = int(num_input)
# 
#   if 0 <= num_input <= 100:
# 
#     print("입력하신 정수는", num_input, "입니다.")
# 
#     if num_input == answer:
#       print("You win!")
#     elif num_input > answer:
#       print("You lose!")
#       print("너무 커요(Too high)") 
#     else: 
#       print("You lose!")
#       print("너무 작아요(Too low)") 
#     
#   else:
# 
#     print("1에서 100사이의 정수만 입력해야 합니다")
#  
# 
# except ValueError:
#   print("정수를 입력하세요")

# 6단계) 참여자가 정답을 맞힐 때까지 입력을 요구하여라.

# answer = 15
# 
# while True:
# 
#   try :
#     
#     num_input = input("1에서 100사이의 정수를 입력하세요 :")
#     num_input = int(num_input)
# 
#     if 0 <= num_input <= 100:
# 
#       print("입력하신 정수는", num_input, "입니다.")
# 
#       if num_input == answer:
#         print("You win!")
#         break
#         
#       elif num_input > answer:
#         print("You lose!")
#         print("너무 커요(Too high)") 
#       else: 
#         print("You lose!")
#         print("너무 작아요(Too low)") 
#       
#     else:
# 
#       print("1에서 100사이의 정수만 입력해야 합니다")
#   
# 
#   except ValueError:
#     print("정수를 입력하세요")

# 7단계) 참여자가 몇 번 시도하여 정답을 맞혔는지를 보여줘라. 

# count_trial = 0
# answer = 15
# 
# while True:
#   
#   try :
#     
#     num_input = input("1에서 100사이의 정수를 입력하세요 :")
#     count_trial = count_trial + 1
#     num_input = int(num_input)
# 
#     if 0 <= num_input <= 100:
# 
#       print("입력하신 정수는", num_input, "입니다.")
# 
#       if num_input == answer:
#         print("You win!")
#         print("시도하신 횟수는: ", count_trial, '번 입니다.')
#         break
#         
#       elif num_input > answer:
#         print("You lose!")
#         print("너무 커요(Too high)") 
#       else: 
#         print("You lose!")
#         print("너무 작아요(Too low)") 
#       
#     else:
# 
#       print("1에서 100사이의 정수만 입력해야 합니다")
#   
# 
#   except ValueError:
#     print("정수를 입력하세요")

# **문제2) 키와 몸무게를 인자로 받아 체질량지수(BMI)를 구하는 코드를 작성하여라. 아래의 사항들을 참고한다.**
# 
# $BMI = \frac{weight}{height^2}$
# 
# * 단위 :
#   * 몸무게(weight) : `kg`
#   * 키(height) : `m`
# 
# * `BMI` 수치에 따른 체중 분류
#   * `BMI <= 18.5` 이면 저체중
#   * `18.5 < BMI <= 23` 이면 정상
#   * `23 < BMI <= 25` 이면 과체중
#   * `25 < BMI <= 30` 이면 비만
#   * `BMI > 30` 이면 고도비만

# weight_input = input("몸무게를 입력해주세요 (kg):")
# weight_input = float(weight_input)
# 
# height_input = input("키를 입력해주세요 (m):")
# height_input = float(height_input)
# 
# BMI = weight_input/(height_input**2)
# 
# if BMI <= 18.5 :
#   print("저체중입니다.")
# 
# elif BMI <= 23 :
#   print("정상체중입니다.")
# 
# elif BMI <= 25 :
#   print("과체중입니다.")
# 
# elif BMI <= 30 :
#   print("비만입니다.")
# 
# else :
#   print("고도비만입니다.")

# **문제3) 두 개의 정수 `a`, `b`를 입력받아 `a/b`를 계산하는 코드를 작성하여라.**
# 
# 단, 아래의 내용을 만족하도록 코드를 작성한다.
# * 정수가 아닌 값이 입력될 경우, 정수를 입력하라고 전달한다.
# * `b`에 `0`이 입력될 경우, 0이 아닌 숫자를 입력하라고 전달한다. 
# * 올바른 값이 입력될 때까지 입력을 요구한다. 

# 
# while True:
# 
#   try :
#     a = int(input("정수 a를 입력해주세요: "))
#     b = int(input("정수 b를 입력해주세요: "))
# 
#     a_over_b = a/b
#     print("a/b = ", a_over_b)
#     break
# 
#   except ValueError:
#     print("정수를 입력해주세요")
# 
#   except ZeroDivisionError:
#     print("0이 아닌 b를 입력해주세요")
# 

# **문제4) 숫자 야구 게임 코드를 작성하여라.**
# 
# 숫자 야구 게임은 임의로 정한 3자리의 수(`ans`)를 참여자가 맞히는 게임으로, 아래의 규칙을 따른다.
# * 사용되는 수는 1~9까지의 서로 다른 정수이다. 
# * 참여자가 입력한 수가 `ans`와 다를 경우, 참여자에게 결과를 알려준다.
#   * 숫자와 위치가 맞으면, 스트라이크
#   * 숫자는 맞지만 위치가 틀리면, 볼
#   * 숫자와 위치가 모두 틀리면, 아웃  
# 
# 예를 들어, ans가 123 일 때, 참여자가 456을 입력하면 '아웃', 257을 입력하면 '1볼', 273을 입력하면 '1볼 1스트라이크'이다. 
# 
# 
# * 각 단계의 내용이 충족되도록 전 단계의 코드를 수정 보완하여라.  
# 예를 들어, 2단계에 작성하는 코드는 1단계와 2단계의 내용이 모두 충족되어야 한다.
# * 3자리 수를 하나 선택하여 `ans` 변수에 할당한다.  
# `ans = 157   # 다른 값으로 변경 가능`
# 
# 1단계) 3자리의 수를 입력받는 코드를 작성하여라.
# > 3자리의 수를 입력하세요 : 

# baseball_input = input("3자리의 수를 입력하세요: ")

# 2단계) 참여자가 입력한 3자리의 수와 `ans`를 비교하여, 스트라이크가 몇 인지를 출력하여라. 

# ans = 157
# ans = str(ans)
# 
# baseball_input = input("3자리의 수를 입력하세요: ")
# 
# count_strike = 0
# 
# for i in range(3):
#   if ans[i] == baseball_input[i]:
#     count_strike += 1
# 
# print(count_strike, " 스트라이크!") 
# 
# 

# ```
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# .
# ```

# 연습을 더 하고 싶다면, 아래의 문제를 풀어보세요!
# 
# **[추가 문제1] 문제4)를 완성해보자.**  
# 3단계) 참여자가 입력한 3자리의 수와 `ans`를 비교하여, 스트라이크와 볼이 몇 인지를 출력하여라.

# ans = 157
# ans = str(ans)
# 
# baseball_input = input("3자리의 수를 입력하세요: ")
# 
# count_strike = 0
# count_ball = 0
# 
# for i in range(3):
# 
#   if ans[i] in baseball_input:
# 
#     if ans[i] == baseball_input[i]:
#       count_strike = count_strike + 1
#     else:
#       count_ball = count_ball + 1
# 
# print(count_strike, " 스트라이크!", count_ball, " 볼!")
#  

# 4단계) 참여자가 입력한 3자리의 수와 `ans`를 비교하여, 아웃이면 아웃을, 아니면 스트라이크와 볼이 몇 인지를 출력하여라.

# ans = 157
# ans = str(ans)
# 
# baseball_input = input("3자리의 수를 입력하세요: ")
# 
# count_strike = 0
# count_ball = 0
# 
# for i in range(3):
# 
#   if ans[i] in baseball_input:
# 
#     if ans[i] == baseball_input[i]:
#       count_strike = count_strike + 1
#     else:
#       count_ball = count_ball + 1
# 
# if count_strike + count_ball == 0:
#   print("아웃!")
# else:
#   print(count_strike, " 스트라이크!", count_ball, " 볼!")
#  

# 들여쓰기를 주의해 주세요!

# 5단계) 참여자가 정답을 맞힐 때까지 입력을 요구하여라.

# ans = 157
# ans = str(ans)
# 
# while True:
# 
#   baseball_input = input("3자리의 수를 입력하세요: ")
# 
#   count_strike = 0
#   count_ball = 0
# 
#   for i in range(3):
# 
#     if ans[i] in baseball_input:
# 
#       if ans[i] == baseball_input[i]:
#         count_strike = count_strike + 1
#       else:1
#         count_ball = count_ball + 1
# 
#   if count_strike + count_ball == 0:
#     print("아웃!")
#   else:
#     print(count_strike, " 스트라이크!", count_ball, " 볼!")
#     if count_strike == 3:
#       print("게임 끝!")
#       break
#   

# 6단계) 숫자가 아닌 값을 입력하면, `숫자를 입력하세요`를 출력하여라.

# ans = 157
# ans = str(ans)
# 
# while True:
# 
#   try:
# 
#     baseball_input = input("3자리의 수를 입력하세요: ")
# 
#     baseball_int = int(baseball_input)
# 
#     count_strike = 0
#     count_ball = 0
# 
#     for i in range(3):
# 
#       if ans[i] in baseball_input:
# 
#         if ans[i] == baseball_input[i]:
#           count_strike = count_strike + 1
#         else:
#           count_ball = count_ball + 1
# 
#     if count_strike + count_ball == 0:
#       print("아웃!")
#     else:
#       print(count_strike, " 스트라이크!", count_ball, " 볼!")
#       if count_strike == 3:
#         print("게임 끝!")
#         break
#   
#   except ValueError:
#     print("숫자를 입력하세요")

# [note] while문은 반드시 loop를 빠져나올 수 있도록 코드를 고려한다

# 7단계) 세 자리 미만의 수를 입력하면, `세 자리의 수를 입력하세요`를 출력하여라.  
# 

# ans = 157
# ans = str(ans)
# 
# while True:
# 
#   try:
# 
#     baseball_input = input("3자리의 수를 입력하세요: ")
# 
#     baseball_int = int(baseball_input)
#     baseball_3digit = baseball_input[2]
#     
# 
#     count_strike = 0
#     count_ball = 0
# 
#     for i in range(3):
# 
#       if ans[i] in baseball_input:
# 
#         if ans[i] == baseball_input[i]:
#           count_strike = count_strike + 1
#         else:
#           count_ball = count_ball + 1
# 
#     if count_strike + count_ball == 0:
#       print("아웃!")
#     else:
#       print(count_strike, " 스트라이크!", count_ball, " 볼!")
#       if count_strike == 3:
#         print("게임 끝!")
#         break
#   
#   except ValueError:
#     print("숫자를 입력하세요")
#     
#   except IndexError:
#     print("세 자리의 수를 입력하세요")

# **[추가문제2] 영어단어를 입력받아 알파벳순으로 출력하는 코드를 작성하여라.**  
# 예를 들어, `dog`를 입력하면, `dgo`를 출력한다.

# word_input = input("영어단어를 입력해주세요 :")
# word_input = word_input.lower() # 소문자로 변환
# 
# word_output = word_input
# 
# for i in range(len(word_input)):
#     
#   minindex = i
#   
#   for j in range(i,len(word_input)):
#     if word_output[j] < word_output[minindex]: 
#       minindex = j
#   
#   word_temp = ""  ## i와 minindex의 위치를 교환하기 위한 temp 변수
# 
#   for k in range(len(word_input)):
# 
#     if k == i:
#       word_temp = word_temp + word_output[minindex]
#     elif k == minindex:
#       word_temp = word_temp + word_output[i]
#     else:
#       word_temp = word_temp + word_output[k]
#     
#   word_output = word_temp
#   
# print("알파벳순 : " + word_output)

# [note] list를 이용하면 간편하게 풀 수 있다.

# **[추가문제3] 다음 중 오류가 발생하는 코드는 무엇인가**
# 
# (a)
# ```
# if 3/0 or True :
#   print("A")
# ```
# 
# (b)
# ```
# if True or 3/0 :
#   print("B")
# ```

# if 3/0 or True :
#   print("A")

# if True or 3/0 :
#   print("B")

# or 연산은 앞이 True이면 뒤를 계산하지 않고 코드를 실행한다! 
