from math import *
import csv

# n1*sin(radians(a1)) = n2*sin(radians(a2))
# n2 = (n1*sin(a1))/sin(a2)

def get_n2(n1, a1_rad, a2_rad):
    return (n1*sin(a1_rad))/sin(a2_rad)


n1 = 1
delta_a1_r = pi/180 # 1deg
delta_a2_r = pi/180 # 1deg

a1_d = list(range(0,50, 5))
a2_d = [0.1,8,11,13,16,20,23,26,28,31]
a1_r = [radians(i) for i in a1_d]
a2_r = [radians(i) for i in a2_d]
delta_sin_a1 = [abs(cos(i) * delta_a1_r) for i in a1_r]
delta_sin_a2 = [abs(cos(i) * delta_a2_r) for i in a2_r]
n2_lst = [get_n2(n1, a1_r[i], a2_r[i]) for i in range(10)]

headers = [
    r'$$\alpha_1 (deg)$$',
    r'$$\alpha_2 (deg)$$',
    r'$$\alpha_1 (rad)$$',
    r'$$\alpha_2 (rad)$$',
    r'$$\Delta sin(\alpha_1)$$',
    r'$$\Delta sin(\alpha_2)$$',
]

csvfile = "test.csv"

with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    i = 0
    max_levels = 10
    writer.writerow(headers)
    while i < max_levels:
        writer.writerow(
            [
                '{}'.format(a1_d[i]),
                '{}'.format(a2_d[i]),
                '{:.4f}'.format(a1_r[i]),
                '{:.4f}'.format(a2_r[i]),
                '{:.4f}'.format(delta_sin_a1[i]),
                '{:.4f}'.format(delta_sin_a2[i]),
            ]
        )
        i = i +1


