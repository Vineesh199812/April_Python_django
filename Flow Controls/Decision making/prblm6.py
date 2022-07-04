total_classes=int(input("number of classes held"))
classes_attended=int(input("numberv of classes attended"))
percentage=(classes_attended/total_classes)*100
print("percentage of classes attended",percentage)
if(percentage>75):
    print("allowed to exam")

else:
    print("not allowed to exam")