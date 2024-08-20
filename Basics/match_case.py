"""
like  c++ switch case in phython it is match case

*but here we dont need to include break in python
*here we can have if statements
*here there can multiple default statements however each one different like differnent if condtion or one without if condtion
*here char , num, whole stings can be be case 




parameter = "Geeksforgeeks"
 
match parameter:
   
    case first  : 
        do_something(first)
     
    case second : 
          do_something(second)
         
    case third : 
        do_something(third)
        .............
        ............
    case n :
        do_something(n)
    case _  : 
          nothing_matched_function()
           """
           
 
def runMatch():
    user = input("Write your username -: ")
 
    # match statement starts here .
    match user:
        case "Om":
            print("Om do not have access  to the database \
            only for the api code.")
        case "Vishal":
            print(
                "Vishal do not have access to the database , \
                only for the frontend code.")
 
        case "Rishabh":
            print("Rishabh have the access to the database")
            print(("Rishabh"))
 
        case _ if user =="":
            print("You do not have any access to the code")
            
        case _:
            print("HELLO")
            
runMatch()