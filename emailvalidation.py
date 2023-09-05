x = 0
for x in range(100):
 print("............Author: Owais Aamir............")
 print(".                                         .")
 print(".                                         .")
 print(".                                         .")
 print(".                                         .")
 email = input("[+] Enter Your Email :")
 k = 0
 b = 0
 c = 0
 if len(email)>=6:
  if email[0].isalpha():
   if ("@" in email) and (email.count("@")==1):
    if (email[-4]==".") ^ (email[-3]=="."):
     for i in email:
      if i==i.isspace():
        k=1
      elif i.isalpha():
       if i==i.upper():
        b=1
      elif i.isdigit:
       continue
      elif i=="_" or i=="." or i=="@":
       continue
      else:
       c=1
     if k==1 or b==1 or c==1:
      print("")
      print("[-] wrong email 5")
     else:
      print("")
      print("[+] Right Email Adress")
    else:
     print("")
     print("[-] Wrong Email 4")
   else:
    print("")
    print("[-] Wrong Email 3")
  else:
   print("")
   print("[-] Wrong Email 2")
 else:
  print("")
  print("[-] Wrong Email 1")

    
    
    
    
    
    
    
    
    
    
    
    