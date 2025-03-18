
#(A):
# count = 0
# class Tracker:
#     def __init__(self):
#         global count
#         count += 1
#
#     def AssignSerialNo(self):
#         return count
#     def __str__(self):
#         return f"I am object no.{self.AssignSerialNo()}"
#
# T1 = Tracker()
# print(T1)
# T2 = Tracker()
# print(T2)
# T3 = Tracker()
# print(T3)

#(B):
class Tracker:
    count = 0
    def __init__(self):
        Tracker.count += 1

    def AssignSerialNo(self):
        return Tracker.count
    def __str__(self):
        return f"I am object no.{self.AssignSerialNo()}"

T1 = Tracker()
print(T1)
T2 = Tracker()
print(T2)
T3 = Tracker()
print(T3)
