import random as rm
def Attendance_check():
    total_attendance=0
    total_absent=0
    attendance={}
    for i in range(1,31):
        attendance[i]=rm.randint(0,1)
    for j in attendance.values():
        if j==0:
            total_attendance+=1
        else:
            total_absent+=1
    print("total leaves in a month : ",total_absent)
    print("Total present in a month : ",total_attendance)
    

Attendance_check()