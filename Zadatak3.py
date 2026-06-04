def lamport_receive(local_time, message_time):
    return max(local_time, message_time) + 1


p1_inc = 5
p2_inc = 6
p3_inc = 2


p1_time = 1 * p1_inc
m1_time = p1_time


p2_time = 2 * p2_inc


p2_time = 3 * p2_inc
m2_time = p2_time


p3_time = 6 * p3_inc


p3_lamport = lamport_receive(p3_time, m2_time)


p3_lamport = p3_lamport + p3_inc
m3_time = p3_lamport


p2_time = 10 * p2_inc


p2_lamport = lamport_receive(p2_time, m3_time)


p2_lamport = p2_lamport + 5 * p2_inc
m4_time = p2_lamport


p1_time = 16 * p1_inc

bez_algoritma = p1_time

sa_lamportom = lamport_receive(p1_time, m4_time)

print("Vreme dolaska m4 na P1 bez algoritma:", bez_algoritma)
print("Vreme dolaska m4 na P1 sa Lamport algoritmom:", sa_lamportom)