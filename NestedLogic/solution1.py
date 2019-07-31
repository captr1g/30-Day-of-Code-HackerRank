# Your local library needs your help! Given the expected and actual return dates for a library book, create
#  a program that calculates the fine (if any). The fee structure is as follows
# 1.If the book is returned on or before the expected return date, no fine will be charged (i.e.:fine = 0.)
# 2.If the book is returned after the expected return day but still within the same calendar month and
# year as the expected return date, fine = 15 * (number of days late).
# 3.If the book is returned after the expected return month but still within the same calendar year as the
# expected return date, the fine = 500 * (number of months late).
# 4.If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000.
Adate = list(map(int,input().split()))
Edate = list(map(int,input().split()))
# check the year is on date or late
if Adate[2]<Edate[2]:
    print(0)
elif Adate[2]==Edate[2]:
    # check the months is on date or late
    if Adate[1]<Edate[1]:
        print(0)
    elif Adate[1]==Edate[1]:
        # check the day is on date or late
        if Adate[0]<Edate[0]:
            print(0)
        elif Adate[0]==Edate[0]:
            print(0)
        else:
            print(15*(Adate[0]-Edate[0]))

    else:
        print(500*(Adate[1]-Edate[1]))
else:
    print(10000)