import math
from prettytable import PrettyTable

izmerenia = [63.739, 63.751,63.737,63.741, 63.743,
             63.740,63.742,63.740,63.741,63.741,
             63.741,63.741,63.741,63.741,63.742,
             63.740,63.740,63.740,63.741,63.741,
             63.740,63.740,63.732,63.742,63.740]

n = len(izmerenia)
sort = 0
while sort != 1:
    uslovie = 1
    sum_pogr = sum(izmerenia)
    srednee_pogr = sum_pogr / n
    tabl = PrettyTable()
    tabl.field_names = ['№', 'x(i)', 'delta * 10^(-3)', 'delta^2 * 10^(-6)']
    delta, delta_2  = [], []
    for i in range(0,  n):
        delta.append(int(round((izmerenia[i] - srednee_pogr), 3) * (10 ** 3)))
        delta_2.append(round(pow(delta[i], 2), 3))
        tabl.add_row([(i + 1), izmerenia[i], delta[i], delta_2[i]])
    sum_del = sum(delta_2)
    print(tabl)
    print(f'\nn = {n} | sum_izm = {round(sum_pogr, 3)}, sred_pogr = {round(srednee_pogr, 3)}\t|\tsum_del^2 = {round(sum_del, 3)}')
    sigma = math.sqrt(sum_del/ n)
    print('Приблеженное значение СКО: ', round(sigma, 3), '* 10^(-3)')
    krit_rayta = int(3 * sigma)
    print('Отклонение по критерию Райта: ', krit_rayta, '* 10^(-3)')
    filt_izm, filt_del, filt_del_2 = [], [], []
    for i in range(0, n):
        if abs(delta[i]) > krit_rayta:
            filt_izm.append(izmerenia[i])
            filt_del.append(delta[i])
            filt_del_2.append(delta_2[i])
            izmerenia.pop(i)
            delta.pop(i)
            delta_2.pop(i)
            sum_del = 0
            n -= 1
            uslovie = 0
            break
    print('\nЗначения, отсеянные по критерию Райта: ', filt_izm, ' ', filt_del, ' ', filt_del_2, '\n')
    if uslovie == 1:
        print('\nДля 99% надежности и 22 измерений коэфф. Стьюдента равен 2,82')
        print('--------------------------Доверительный интервал------------------------------')
        eps = 2.82 * math.sqrt(sum_del / (n * (n - 1)))
        for x in range(0, n):
            print(f'{round(srednee_pogr, 3)} - {round(eps, 5)} * 10^(-3)\t<\t{izmerenia[x]}\t<\t{round(srednee_pogr, 3)} + {round(eps, 5)} * 10^(-3) = 0,99')
        sort = 1
        break
