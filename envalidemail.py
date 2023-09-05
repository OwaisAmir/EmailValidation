print("............Author: Owais Aamir............")
email = input("[+]Enter Your Email:")
A = 0
B = 0
C = 0
if len(email)>=6:
 if email[0].isalpha():
  if ("@" in email) and (email.count("@")==1):
   if (email[-4]==".") ^ (email[-3]=="."):
    for i in email:
     if i==i.isspace():
       A=1
     elif i.isalpha():
      if i==i.upper():
       B=1
     elif i.isdigit:
      continue
     elif i=="_" or i=="." or i=="@":
      continue
     else:
      C=1
    if A==1 or B==1 or C==1:
     print("wrong email 5")
    else:
     print("Right Email Adress")
   else:
    print("Wrong Email 4")
  else:
   print("Wrong Email 3")
 else:
  print("Wrong Email 2")
else:
 print("Wrong Email 1")

    
    
    
    
    
    
    
    
    
    
    
    