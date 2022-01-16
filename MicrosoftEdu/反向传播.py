

def stage2(x,y):
    return x*y
def stage1(w,b):
    return 2*w+3*b,2*b+1



label=150
loss=1.0
w=3.0
b=4.0
while abs(loss)>0.001 :
    x,y=stage1(w,b)
    z=stage2(x,y)
    loss=z-label
    delta_b=(loss/2)/(3*y+2*x)
    delta_w=(loss/2)/(2*y)
    w-=delta_w
    b-=delta_b
print(w,b)
