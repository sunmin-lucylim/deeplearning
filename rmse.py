import numpy as np

# 기울기 a와 절편 b 
ab = [3, 76]

# x, y 데이터 값 (x는 공부시간, y는 실제 점수임)
data = [[2,81],[4,93],[6,91],[8,97]]
x = [i[0] for i in data]
y = [i[1] for i in data]

# y=ax+b에 값 대입해서 결과 출력하는 함수 (예측값)
def predict(x)
    return ab[0]*x + ab[1]

# RMSE 함수 
def rmse(p,a)
    return np.sqrt(((p-a)**2).mean())

# RMSE 함수를 각 y값에 대입해서 최종값 구하기
def rmse_val(predict_result, y):
    return rmse(np.array(predict_result), np.array(y))

# 예측값이 들어가는 빈 리스트
predict_result = []

# 모든 x값을 한번씩 대입해서 예측값 내보기 
for i in range(len(x)):
    # predict_result 리스트 완성하기
    predict_result.append(predict(x[i]))
    print("공부한 시간=%.f, 실제점수=%.f, 예측점수=%.f" % (x[i],y[i],predict(x[i])))

# 최종 RMSE 출력 
print("rmse 최종값:"+ str(rmse_val(predict_result,y)))
