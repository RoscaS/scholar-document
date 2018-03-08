@import "static/style.html"


# Labo de physique 1: Réfraction 

Cras *pellentesque* volutpat dui. Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. Nulla justo. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. `Nunc rhoncus dui vel sem`. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. 

>Proin interdum mauris non ligula pellentesque ultrices. Nullam porttitor lacus at turpis. Vivamus vel nulla eget eros elementum pellentesque. Morbi non lectus.

```python {cmd="/usr/bin/python3" matplotlib=true hide}
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from math import *

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
sin_a1 = [abs(cos(i) * delta_a1_r) for i in a1_r]
sin_a2 = [abs(cos(i) * delta_a2_r) for i in a2_r]
n2_lst = [get_n2(n1, a1_r[i], a2_r[i]) for i in range(10)]

x = delta_sin_a1
y = delta_sin_a2

fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit) 

matplotlib.rcParams.update({'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'})
fig, axes = plt.subplots(figsize=(5,2), dpi=1080)
fig.subplots_adjust(bottom=0.2)
axes.legend(loc=2);  # upper left corner
axes.set_xlabel('$sin(\\alpha_1)$')
axes.set_ylabel('$sin(\\alpha_2)$')
axes.set_title('Situation 1 $sin(\\alpha_1)=n_2 sin(\\alpha_2)$');

plt.plot(x,y, 'bo', label=r"$y=mx+b $", marker='+', markersize=12)
plt.plot(x, fit_fn(x), 'r', label=r"fit")
axes.legend(loc=2)

plt.xlim(0.012, 0.018)
plt.ylim(0.014, 0.018)
plt.show() # show figure
```



<!-- <img src="/assets/matlab_two_axes_plot_style.png" height="300px"> -->


## Poule
Duis bibendum. `Etiam` justo. Proin at turpis a pede posuere nonummy. Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. Nullam orci pede, venenatis non, sodales sed, **tincidunt** eu, felis. Vivamus tortor. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. **Nulla** ut erat id mauris vulputate elementum. Sed ante. Phasellus sit amet erat. Aenean auctor gravida sem. Duis aliquam convallis nunc. Donec semper sapien a libero. Sed sagittis. Mauris lacinia sapien quis libero. Praesent blandit. Vestibulum ac est lacinia nisi venenatis tristique. Quisque ut erat. Curabitur convallis. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.

## Cochon

Vivamus tortor. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Nulla ut erat:

* Proin at turpis a pede posuere nonummy
* Imperdiet et, commodo vulputate
* Praesent blandit

$$n_1sin(\alpha_1)=n_2sin(\alpha_2)$$

>Nullam porttitor lacus at turpis. Vivamus vel nulla eget eros elementum pellentesque. Morbi non lectus.


$$
\sum_{n=1}^\infty \frac{1}{n^2} \to
\textstyle \sum_{n=1}^\infty \frac{1}{n^2} \to
\displaystyle \sum_{n=1}^\infty \frac{1}{n^2}
$$

Erat id mauris vulputate elementum. Sed ante. Phasellus sit amet erat. Aenean auctor gravida sem. Duis aliquam convallis nunc. Donec semper sapien a libero.


In porttitor pede justo eu massa. **Nulla** ut erat id mauris vulputate elementum. Sed ante. Phasellus sit amet erat. Aenean auctor gravida sem. Duis aliquam convallis nunc. Donec semper sapien a libero. Sed sagittis.


$$ 
\left\{ \begin{array}{l}
0 = c_x-a_{x0}-d_{x0}\dfrac{(c_x-a_{x0})\cdot d_{x0}}{\|d_{x0}\|^2} + c_x-a_{x1}-d_{x1}\dfrac{(c_x-a_{x1})\cdot d_{x1}}{\|d_{x1}\|^2} \\[2ex] 
0 = c_y-a_{y0}-d_{y0}\dfrac{(c_y-a_{y0})\cdot d_{y0}}{\|d_{y0}\|^2} + c_y-a_{y1}-d_{y1}\dfrac{(c_y-a_{y1})\cdot d_{y1}}{\|d_{y1}\|^2} \end{array} \right. 
$$

Proin at turpis a pede posuere nonummy. Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo.


```python {class=line-numbers}
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
```


Aliquam erat volutpat. Donec ut dolor. Sed vel enim sit amet nunc viverra dapibus. In hac habitasse platea dictumst. Praesent blandit lacinia erat.

$$\mu_0=4\pi\times10^{-7} \ \left.\mathrm{\mathrm{T}\!\cdot\!\mathrm{m}}\middle/\mathrm{A}\right.$$

Aenean auctor gravida sem. Duis aliquam convallis nunc. Donec semper sapien a libero. Sed sagittis. Mauris lacinia sapien quis libero. Praesent blandit. Vestibulum ac est lacinia nisi venenatis tristique. Quisque ut erat. Curabitur convallis. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.


## Poney

Aliquam non mauris. Praesent blandit. In hac habitasse platea dictumst. Maecenas pulvinar lobortis est. Mauris sit amet eros.
Sed ante. Phasellus sit amet erat. Aenean auctor gravida sem. Duis aliquam convallis nunc. Donec semper sapien a libero. Sed sagittis. Mauris lacinia sapien quis libero. Praesent blandit. Vestibulum ac est lacinia nisi venenatis tristique. Quisque ut erat. Curabitur convallis. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.
Aliquam non mauris. Praesent blandit. In hac habitasse platea dictumst. Maecenas pulvinar lobortis est. Mauris sit amet eros.


@import "data.csv" 


<br>

