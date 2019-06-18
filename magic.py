import csv


argumentsToBeAdded = ', Sub-task, Please look at the description at Parent Task'
listOfTickets = ['OPS-213563', 'OPS-213696', 'OPS-213697','OPS-213705','OPS-213706','OPS-213707','OPS-213708','OPS-213709','OPS-213710','OPS-213711','OPS-213712']
content = []
count = 1
ticketNo = 0
f = open('zmientenplik.txt', 'r')
for x in f:
   placeholder = str(count) + ') ' + x.split('/',2)[-1].strip() + ', ' + listOfTickets[ticketNo] + argumentsToBeAdded
   content.append(placeholder.split(','))
   count += 1
   if count == 257:
      if ticketNo != 10:
         count = 0
         ticketNo += 1

numberOfFiles = 0
columns = ['Summary','Parent ID','Ticket Type','Description']
while len(content) != 0:
   with open('jiraTickets' + str(numberOfFiles) + '.csv', 'a') as outcsv:
      writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')  
      writer.writerow(columns)
      for item in content[:249]:
         writer.writerow([item[0], item[1], item[2], item[3]])
      content = content[249:]
      numberOfFiles += 1
