import csv
file=open("data.csv","w",newline="")
writer=csv.writer(file)
writer.writerow(["Name","Age","Branch"])
writer.writerow(["Likitha",21,"AI&DS"])
file.close()