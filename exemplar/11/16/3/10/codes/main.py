#E1 is the event that promotion of John
#E2 is the event that promotion of Rita
#E3 is the event that promotion of Aslam
#E4 is the event that promotion of Gurpreet

E1 = 1
E4 = E1
E2 = 2*E1
E3 = 4*E1

p_total = E1 + E2 + E3 + E4
print("E1 = ",E1/p_total)
print("E2 = ",E2/p_total)
print("E3 = ",E3/p_total)
print("E4 = ",E4/p_total)


print("E1 + E4 = ",(E1 + E4)/p_total)
