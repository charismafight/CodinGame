surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]
last_v_speed=0
# game loop
while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    if v_speed <-35:
        if power !=4:
            power+=1
    elif v_speed >-30:
        if power != 0:
            power-=1
    print("0 "+str(power))
