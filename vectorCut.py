
def vectorCut(N, M):
  avgPart = float(N / M)                                        #Средний размер каждой части вектора.
  shift = 0                                                     #Величина отступа от начала вектора.
  avgPartCurrent = avgPart                                      #Фактический размер каждого отрезка.

  if int(avgPart) - avgPart != 0:                               #Если средняя длина отрезка - десятичное число.
    decimalSign = 1                                             #Позиция десятичного знака. После запятой.
    avgPartCurrent = avgPart * 10                               #Для проверки 1-го десятичного знака.
    while int(avgPartCurrent) % 10 == 0:                        #Находим позицию не нулевого десятичного знака.
      avgPartCurrent *= 10
      decimalSign += 1
    avgPartCurrent = round(int(avgPart * 10 ** decimalSign) / float(10 ** decimalSign), 4)    #Средний размер отрезка вектора
                                                                                              #с учётом отступов.
    shift = (N - avgPartCurrent * M) / 2                                            #Величина отступа.

  for i in range(M - 1):                                                            #Вывод координат отрезков.
    print('[', round(i * avgPartCurrent + shift, 4), '; ',
          round(i * avgPartCurrent + shift + avgPartCurrent, 4), ')', sep = '')
  M -= 1
  print('[', round(M * avgPartCurrent + shift, 4), '; ',
        round(M * avgPartCurrent + shift + avgPartCurrent, 4), ']', sep = '')
                                                            #Отдельно выводим координаты последнего отрезка,
                                                            #чтобы закрыть квадратной скобкой.
vectorCut(10, 3)

