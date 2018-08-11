'''
Complete the timeConversion function in the editor below. It should return a new string
representing the input time in 24 hour format.

timeConversion has the following parameter(s):

s: a string representing time in  hour format

input format = 07:05:45PM
output format =19:05:45
'''


x= input('Enter time')
hr = int(x[0:2])
rest = x[2:-2]
mer = x[-2:]

if hr>= 12 and mer.lower()=='am':
    hr = '00'
    time = hr+rest
elif mer.lower()=='am':
    hr = '0'+str(hr)
    time = hr+rest
elif hr>12 and mer.lower()=='pm':
    hr = str(hr+12)
    time= hr+rest
elif hr == 12 and mer.lower()=='pm':
    hr = '00'
    time = hr+rest
        
     
    
print(time)   
    