a = input('time_input:')
a_int = int(a)

a_m = a_int//100
a_s = a_int % 100
#a
b = input('time_input:')
b_int = int(b)

b_m = b_int//100
b_s = b_int % 100

t_m = a_m-b_m
t_s = a_s-b_s

if(t_s < 0):
    t_s = 60 - (t_s*-1)
    t_m -= 1


print(t_m)
print(t_s)