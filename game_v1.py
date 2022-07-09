from statistics import mean
import numpy as np

def random_predict() -> int:
    """угадывает число

    Returns:
        int: число попыток
    """

    
    count = 0
    number = np.random.randint(1, 101)
    while True:
        count += 1
        if count == 1:
            predict_num = 50
            temporary_value = 25
            if predict_num == number:
                break
        elif predict_num < number:
            predict_num += temporary_value
            temporary_value = round(temporary_value/2 + 0.01)
        elif predict_num > number:           
            predict_num -= temporary_value
            temporary_value = round(temporary_value/2 + 0.01)
        else:
            break
    return count

lst = []
for i in range(0, 100):
    lst.append(random_predict())
print(mean(lst))


