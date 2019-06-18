argumentsToBeAdded = ' , Sub-task, Please look at the description at Parent Task'
listOfTickets = [', OPS-213563', ', OPS-213696', ', OPS-213697',', OPS-213705',', OPS-213706',', OPS-213707',', OPS-213708',', OPS-213709',', OPS-213710',', OPS-213711',', OPS-213712',]
content = []
count = 1
ticketNo = 0
f = open('TwojPlik.txt', 'r')
for x in f:
   content.append(str(count) + ') ' + x.split('/',2)[-1].strip() + tickets[ticketNo] + arguments)
   count += 1
   if count == 257:
      if ticketNo != 10:
         count = 0
         ticketNo += 1

with open ("JiraTicketFormat.txt","w")as fw:
   fw.write('\n'.join(content))
