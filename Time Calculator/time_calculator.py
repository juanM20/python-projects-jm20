
def add_time(time, time2):
  


  print(time.find(' '), time2.find(':'))

  time1 = time.split(' ')
  day = time1[1]
  [t1_h, t1_m] = time1[0].split(':') 
  [t2_h, t2_m] = time2.split(':')
  print(t1_h, t1_m, t2_h, t2_m)
  result = time + time2
  return result