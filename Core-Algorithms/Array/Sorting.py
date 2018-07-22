def BubbleSort(a):
  n = len(array)
  for i in range(n):
      for j in range(n-i-1):
          if a[j] > a[j+1]:
              N += 1
              a[j], a[j+1] = a[j+1], a[j]       
