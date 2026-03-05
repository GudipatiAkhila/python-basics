#  python is case sensitive  it takes only small letters 
# in the below i have given capital - PROD letters it is not taking 
# if we want to convert capital to small bcz users given any type either it captial or small and combination of both 
# for that we use casefold - it everything convrt into small letters 

#environment = "PROD"
environment = input("Enter your environment: ")
change_ticket = False


environment = environment.casefold()

if environment == "prod":
    change_ticket == True
    print("please provide a change ticket ") 
elif environment == "staging":
    print("welcome to staging environment")

else:
    print("please login using your credentials")
# now i have given captial right but it will give us ouput as we expected 
# please provide a change ticket - output 

