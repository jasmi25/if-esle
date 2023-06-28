#25.A student will not be allowed to sit in an exam if his/her attendance is less than
#75%.Take following input from the user. Number of classes held. Number of
#classes attended. And print, percentage of class attended. Is the student is
#allowed to sit in the exam or not.
held=int(input("enter Number of classes held:- "))
attended=int(input("enter Number of classes attended:- "))
percentage=attended*75/100
if percentage>75:
    print("allowed for sit in the exam=",percentage)
else:
    print("not allowed for sit in the exam=",percentage)
