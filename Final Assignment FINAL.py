#########  CMPT 120  FINAL ASSIGNMENT 
#########  VERA YANG  301272027
#########  Dec 3, 2018



import sys
import turtle as t


## BOOLEAN VARIABLE THAT ALLOWS THE PROGRAM TO KEEP RUNNING AS LONG AS THE USER DOESN'T END IT
end = False



## WELCOME THE USER
print ("\nWelcome to the CMPT 120 6-49 Processing system!")
print ("============================================================================")



## EVERYTIME THE PROGRAM IS RUN, PRINT THE FOLLOWING CODE ONCE RIGHT AT THE BEGINNNING
## INFORM THE USER WHAT TO DO AND ASK THEM FOR AN INPUT FILE
print ("\nYou first need to provide the input file name")
print ("You will be asked to provide the output file name later\n")

print ("The input file should be in this folder")
print("The output file will be created in this folder\n")

print ("You will be able to provide new names for the file or accept the default names.")
print ("Both files should have the extension .csv\n")

file_name = input("Type x for INPUT file name 'IN_data_draws3.csv', or a new file name ==> ")

## IF THE USER TYPES "x", THE PROGRAM WILL IMPORT A DEFAULT FILE (IN_data_draws3.csv)
if file_name == "x":
    file_name = "IN_data_draws20.csv"



## ONCE THE USER DECIDES WHICH CSV FILE TO IMPORT INTO THE PROGRAM,
## IMPORT THE CSV FILE
def read_csv_into_list_of_lists(IN_file):
    '''
    PROVIDED. CMPT 120
    A csv file should be available in the folder (where this program is)
    A string with the name of the file should be passed as argument to this function
    when invoking it
    (the string would include the csv extension, e.g "ID_data.csv")
    '''

    import csv

    lall = []
 
    print("\n.... TRACE - data read from the file\n")
    with open(IN_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for inrow in csv_reader:
            print(".......",inrow)
            lall.append(inrow)

    return lall

## APPEND EVERYTHING INTO A GLOBAL VAIRABLE LIST CALLED "lists_all"
lists_all = read_csv_into_list_of_lists(file_name)



## ASKS THE USER WHAT THEY WANT THE PROGRAM TO DO:
## ["ALL" TO PROCESS ALL THE DATA]  ["SEL" TO PROCESS SELECTED MONTH OF DATA]  ["END" TO END THE PROGRAM]
## WILL RETURN USER'S INPUT AND PASS IT TO THE FUNCTION BELOW AS AN ARGUMENT FOR VALIDATION
def ask_user_for_input():

    print("\n============================================================================")
    print("Please choose one of the three options:\n")
    print("Type ALL to process all the data")
    print("Type SEL to process selected draws")
    print("Type END to end this program\n")
    
    users_choice = input("Type ALL, SEL, or END (not case sensitive) ==> ")

    return users_choice



## VALIDATES USER'S INPUT: ALL, SEL, OR END
## WILL KEEP ASKING IF USER'S INPUT IS INVALID
## RETURNS THE MODE OF THE PROGRAM BASED ON USER'S INPUT, THEN THE PROGRAM WILL DECIDE WHICH DATA TO PROCESS BASED ON THE MODE
def starthere(choice):

    correct_input = False
    options = ["all_data", "sel", "end", "ask_again"]   ## ALL THE MODES THAT THE PROGRAM CAN BE IN
    

    ## WHILE THERE IS NO VALID INPUT, SUCH AS ALL, SEL, AND END
    ## THE PROGRAM WILL KEEP ASKING USER FOR AN INPUT
    while correct_input == False:
        

        ## IF USER INPUTS "ALL"
        if (len(choice) == 3 and (choice[0] == "A" or choice[0] == "a") and (choice[1] == "L" or choice[1] == "l") and
            (choice[2] == "L" or choice[2] == "l")):
            print("ALL the data will be processed")
            month_choice = -1
            mode = options[0]       ## THE MODE OF THE PROGRAM TURNS TO "ALL", WHICH PROCESSES ALL THE DATA
            correct_input = True    ## VALID INPUT TURNS TRUE, SO STOP ASKING
##            print ("TRACE: ", mode, correct_input)

        ## IF USER INPUTS "SEL"            
        elif(len(choice) == 3 and (choice[0] == "S" or choice[0] == "s") and (choice[1] == "E" or choice[1] == "e") and
            (choice[2] == "L" or choice[2] == "l")):
            print("SELECTED data will be processed")

            print("\nPlease select a month\nOnly data associated to this month will be processed\n")
            mode = options[1]       ## THE MODE OF THE PROGRAM TURNS TO "SEL", WHICH PROCESS SELECTED DATA
            correct_input = True    ## VALID INPUT TURNS TRUE, SO STOP ASKING
##            print ("TRACE: ", mode, correct_input)
            

        ## IF USER INPUTS "END"
        elif(len(choice) == 3 and (choice[0] == "E" or choice[0] == "e") and (choice[1] == "N" or choice[1] == "n") and
            (choice[2] == "D" or choice[2] == "d")):
            print("BYE!!!!! The program has ended.")
            correct_input = True    ## VALID INPUT TURNS TRUE, SO STOP ASKING
            sys.exit()              ## EXIT THE PROGRAM
##            print ("Trace: ", mode, correct_input)

        else:
            print("Your option is invalid. Please try again!\n")
            mode = options[3]        
            correct_input = True    ## ALLOWS "Your option is invalid. Please try again!" TO ONLY PRINT ONCE
                                    ## WHILE THERE IS NO VALID USER INPUT

    return mode



## WILL BE CALLED IF THE USER INPUT IS "SEL"
## DETECTS WHICH MONTH THE USER SELECTED AND SORT THE CORRESPONDING DATA INTO A LIST
## RETURNS THE LIST TO ANOTHER FUNCTION FOR FURTHER ARRANGEMENT
def detecting_month(lall):

    month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    dates = []
    numbers_drawn = []
    jackpot = []
    winners_num = []
    receive_all_lists = []
    yes_month = False

    lall_length = len(lall)

##    print ("in detecting month")


    ## WHILE THE IMPORTED DATA DOES NOT HAVE A MONTH THAT THE USER SELECTED,
    ## KEEP ASKING THE USER TO CHOOSE ANOTHER MONTH
    while yes_month == False:

        print("Not all the months have corresponding data, you will be asked again to choose another month if this is the case")
        month_choice = input("Please type a month number (1 to 12) ==> ")
        

        if (month_choice.isdigit() == False):
            print ("That was not an integer. Please retype\n")
            
     
        elif (month_choice.isdigit()):

            if (int(month_choice) < 1 or int(month_choice) > 12):
                print ("The month number is out of range. Please retype\n")
                

            for i in range(lall_length):

                for k in range(0, 1):

                    first_dash = lall[i][k].index("-")
                    second_dash = first_dash + 4

                    m_name = lall[i][k][first_dash+1:second_dash]   ## SHOWS MONTH IN ALPHABET
                    m = month_list.index(m_name)+1    ## SHOWS MONTH IN NUMBERS

                    if (int(month_choice) == m):
                        yes_month = True            ## TURNS TRUE WHEN THE IMPORTED DATA HAS A MONTH THAT THE USER SELECTED

                        ## THE DATES FOR EACH DRAW WILL BE ADDED TOGETHER AS A LIST
                        dates.append(lall[i][k]) 

                        ## print (m_name, m, month_choice)


                        ## THE NUMBERS DRAWN FOR EACH DRAW WILL BE ADDED TOGETHER AS A LIST
                        la = []
                        for k in range(1, 8):
                            la.append(int(lall[i][k]))
                        numbers_drawn.append(la)

                        ## THE JACKPOT FOR EACH DRAW WILL BE ADDED TOGETHER AS A LIST
                        for k in range(8, 9):
                            jackpot.append(lall[i][k])
                            
                        ## THE NUMBER OF WINNERS FOR EACH DRAW WILL BE ADDED TOGETHER AS A LIST
                        for k in range(9, 10):
                            winners_num.append(lall[i][k])

            ## ALL THE CORRESPONDING DATES, NUMBERS, JACKPOTS, AND WINNERS# ARE ADDED TOGETHER AS A LIST
            receive_all_lists.append(dates)
            receive_all_lists.append(numbers_drawn)
            receive_all_lists.append(jackpot)
            receive_all_lists.append(winners_num)
##            print (receive_all_lists)

    return receive_all_lists



## WILL BE CALLED IF THE USER INPUT IS "ALL"
## ADD EVERYTHING TOGETHER AS A LIST AND RETURN THE LIST TO ANOTHER FUNCTION FOR FURTHER ARRANGEMENT
def process_all_data(lall):

    dates = []
    numbers_drawn = []
    jackpot = []
    winners_num = []
    receive_all_lists = []

    lall_length = len(lall)
    
    for i in range(lall_length):
        for k in range(0, 1):
            dates.append(lall[i][k])
##    print (dates, "in process all data")

    for i in range(lall_length):
        la = []
        for k in range(1, 8):
            la.append(int(lall[i][k]))
        numbers_drawn.append(la)
            

    for i in range(lall_length):
        for k in range(8, 9):
            jackpot.append(lall[i][k])

    for i in range(lall_length):
        for k in range(9, 10):
            winners_num.append(lall[i][k])

    receive_all_lists.append(dates)
    receive_all_lists.append(numbers_drawn)
    receive_all_lists.append(jackpot)
    receive_all_lists.append(winners_num)
##    print (receive_all_lists)
    
    return receive_all_lists



def convert_lall_to_separate_lists(mode):

##    print (mode)
    

    ## IF THE THE MODE OF THE PROGRAM IS "ALL"
    if mode == "all_data":

##        print ("TRACE: GOING TO CREATE LIST IF ALL DATA")

        ## CALL THE "process_all_data" FUNCTION AND RECEIVE THE LIST THAT IT RETURNS
        receive_data = process_all_data(lists_all)

        
##        print (receive_data)
        

        ## CREATES A LIST WITH ONLY DATES FROM THE BIG LIST IT RECEIVES
        date_list = []
        for i in range(0, 1):
            date_list = date_list + receive_data[i]
##        print (date_list)

        ## CREATES A LIST WITH ONLY THE NUMBERS DRAWN FROM THE BIG LIST IT RECEIVES
        numbers_list = []
        for i in range(1, 2):
            numbers_list = numbers_list + receive_data[i]

        ## CREATES A LIST WITH ONLY THE JACKPOTS FROM THE BIG LIST IT RECEIVES    
        jackpot_list = []
        for i in range(2, 3):
            jackpot_list = jackpot_list + receive_data[i]

        ## CREATES A LIST WITH ONLY THE NUMBER OF WINNERS FROM THE BIG LIST IT RECEIVES
        winner_list = []
        for i in range(3, 4):
            winner_list = winner_list + receive_data[i]


    ## IF THE MODE OF THE PROGRAM IS "SEL"
    elif mode == "sel":

##        print ("TRACE: GOING TO CREATE LIST OF SELECTED DATA")

        ## CALL THE "detecting_month" FUNCTION AND RECEIVE THE LIST IT RETURNS
        receive_data = detecting_month(lists_all)
        
        date_list = []
        for i in range(0, 1):
            date_list = date_list + receive_data[i]
##        print(date_list)

        numbers_list = []
        for i in range(1, 2):
            numbers_list = numbers_list + receive_data[i]
##        print (numbers_list)

        jackpot_list = []
        for i in range(2, 3):
            jackpot_list = jackpot_list + receive_data[i]
##        print (jackpot_list)

        winner_list = []
        for i in range(3, 4):
            winner_list = winner_list + receive_data[i]
##        print (winner_list)


    return date_list, numbers_list, jackpot_list, winner_list, mode

    

## SHOWS THE DETAILS OF THE DRAWS THAT ARE BEING PROCESSED AND EXPORTED
## INCLUDING THE DRAWS' DATE, NUMBERS DRAWNS, JACKPOT, AND # OF WINNERS
def show_details_of_each_draw(date, numbers, jackpot, winner):

    print ("\nJUST TO TRACE, the draw being processed is:")
    for i in range(len(date)):
        print ("\nindex# " + str(i))
        print("Date:", date[i])
        print("Numbers drawn:", numbers[i])
        print("Jackpot:", jackpot[i])
        print("Num winners:", winner[i])

    return



## FIND THE MAXIMUM JACKPOT OUT OF ALL THE DRAWS PROCESSED
## RECEIVE THE "jackpot_list" AND "date_list" AS PARAMETERS
def find_max_jackpot(jackpot, date):

    max_jackpot = -1
    max_jackpot_pos = -1

    for i in range(len(jackpot)):
        if (int(jackpot[i]) > max_jackpot):
            max_jackpot = int(jackpot[i])
            max_jackpot_pos = i
##        print (max_jackpot, max_jackpot_pos)

    ## RETURN THE MAXIMUM JACKPOT AND ITS DATE
    result = "max jackpot " + str(max_jackpot) + "\ndate max jackpot " + str(date[max_jackpot_pos])
    
    return result



## CALCULATE THE AVERAGE MONEY WON FOR EACH DRAW DEPENDING ON THE # OF WINNERS
## RECEIVE THE jackpot_list AND winner_list AS PARAMETERS
def calculate_average_won(jackpot, winner):  

    ## CREATE A LIST OF THE AVERAGE AMOUNT OF MONEY WON FOR EACH DRAW
    average_won_list = []

    for i in range(len(jackpot)):
        if (int(winner[i]) == 0):       ## IF A DRAW HAS NO WINNER, THEN THE AVERAGE MONEY WON IS ZERO
            average_won_list.append(0)
        else:
            average_won = float(jackpot[i])/int(winner[i])      ## ELSE DIVIDE THE JACKPOT BY THE # OF WINNERS FOR THE DRAW
            average_won_list.append(average_won)
            
##        print (average_won_list)
            
    return average_won_list



## FROM THE THE "average_won_list", FIND THE MAXIMUM AMOUNT OF THE MONEY WON
## RECEIVE "average_won_list" AND "date_list" AS PARAMETERS
def find_max_won(average_won, date):

    max_won = -1
    max_won_pos = -1
    result = ""


    for i in range(len(average_won)):
        if (average_won[i] > max_won):
            max_won = average_won[i]
            max_won_pos = i    ## FIND THE DATE FOR THE MAXIMUM AMOUNT OF MONEY WON

##        print (max_won, max_won_pos)

    return "\nmax average won " + str(max_won) + "\ndate max average won " + str(date[max_won_pos])



## GO THROUGH THE NUMBERS THAT ARE DRAWN FROM ALL THE DRAWS
## COUNT HOW MANY TIMES A NUMBER IS DRAW
## RECEIVE "numbers_list" AS PARAMETER
def count_each_number_drawn(numbers):

    count_number_drawn = [0]*50

    for i in range(len(numbers)):
        for k in range(0, 7):
                ndig = numbers[i][k]
                count_number_drawn[ndig] += 1

##                print "TRACE ======>"
##                print ndig, ",i is", i, ",k is", k
##                print(count_number_drawn)

    return count_number_drawn



## GO THROUGH THE NUMBERS THAT ARE DRAWM FROM ALL THE DRAWS
## DISTRIBUTE THE NUMBERS INTO 5 INTERVALS
def range_for_all_draws(numbers):

    count_number_range = [0]*5
    range_limit = 0

    while range_limit < 50:

        for i in range(len(numbers)):
            for k in range(0, 7):
                if (range_limit*10 < numbers[i][k] <= (range_limit+1)*10):
##                    print (numbers[i][k], "range: (", range_limit*10, ",", (range_limit+1)*10, "]")
                    count_number_range[range_limit] += 1
        range_limit += 1
        
    return count_number_range



## GO THROUGH EACH DRAW
## FOR EACH DRAW DISTRIBUTE THE NUMBERS INTO ITS OWN 5 INTERVALS
def range_for_each_draw(numbers):

    a = 0
    all_range_for_each_draw = []

    while a < len(numbers):

        range_limit = 0
        each_range = [0]*5
        
        while range_limit < 50:

            for k in range(0, 7):
                if (range_limit*10 < numbers[a][k] <= (range_limit+1)*10):
                    each_range[range_limit] += 1

            range_limit += 1

        a += 1
        all_range_for_each_draw.append(each_range)
##        print (all_range_for_each_draw)
 
    return all_range_for_each_draw



## GO THROUGH THE NUMBERS THAT ARE DRAWN FROM ALL THE DRAWS
## COUNT THE TOP 6 NUMBERS THAT GET DRAWN THE MOST
def frequently_drawn_numbers():

    repeat = 0
    res = ""
    count_each_number_copy = [] + receive_count_each_number

    while repeat < 6:   ## REPEAT THE PROCESS 6 TIMES TO GET TOP 6 NUMBERS
        max_frequency = count_each_number_copy[0]
        pos = 0
        
        for i in range(len(count_each_number_copy)):
            if (count_each_number_copy[i] > max_frequency):
                max_frequency = count_each_number_copy[i]
                pos = i
##                print (pos, count_each_number_copy[i])
                
        res = res + "number " + str(pos) + " was drawn " + str(max_frequency) + " times\n"
##        print (res)
##        print (count_each_number_copy)
        count_each_number_copy[pos] = -1
        repeat += 1
        
    return res



## TURTLE FUNCTION
## DRAWS THE GRAPH OF THE DISTRIBUTION OF THE NUMBERS
## RECEIVE RESULT FROM "range_for_all_draws" AS AN ARGUMENT
def turtle_graph(number_range):


    ## ASK IF THE USER WANT TO DRAW THE GRAPH
    draw_graph = input("Would you like to graph the ranges distribution? (Y/N) ==> ")
    draw = False    ## BOOLEAN VARIABLE CONTROLLING WHETHER TO DRAW THE GRPAH OR NOT


    ## IF THE USER WANTS TO DRAW THE GRAPH, SWITCH THE VARIABLE "draw" TO TRUE
    if draw_graph == "Y" or draw_graph == "y":
        draw = True

    ## WHILE THE VARIABLE "draw" IS TRUE, DRAW THE FOLLOWING CODE
    while draw == True:
        t.clearscreen()
        t.colormode(255)
        t.penup()

        ## Drawing axis
        t.goto(-150, 100)
        t.right(90)
        t.down()
        t.fd(150)
        t.left(90)
        t.fd(300)

        t.setheading(180)
        t.fd(270)

        ## THIS IS THE CODE FOR DRAWING ONE BAR (ONE INTERVAL) AT A TIME
        ## REPEAT 5 TIMES BECAUSE THERE ARE 5 INTERVALS TO DRAW
        i = 0
        while i < 5:
            t.pencolor("#83a5a5")
            t.fillcolor("#83a5a5")
            t.begin_fill()

##            print (number_range[i])
            t.setheading(90)
            t.fd(number_range[i]*5)     ## MULTIPLY THE RESULT FOR EACH INTERVAL BY 5 SO THAT THE BARS WON'T LOOK TOO SHORT
            t.right(90)
            t.fd(20)
            t.right(90)
            t.fd(number_range[i]*5)
            t.left(90)
            t.up()
            t.fd(30)
            t.down()
            t.left(90)
            t.end_fill()
            i +=1
        draw = False    ## CHANGING THE BOOLEAN "draw" TO FALSE HERE ALLOWS THE GRAPH TO BE DRAWN ONLY ONCE

    return



## CONCATENATE THE RESULT FOR EACH SELECTED DRAW AND RETURN THE STRINGS
## THE RESULT INCLUDES ITS DATE, DISTRIBUTION OF RANGE INTERVAL, AND AVERAGE AMOUNT OF MONEY WON 
def append_1_draw_to_output_list(date, lfreq_ran, avg_paid):

    lout = ""
    
##    PROVIDED. CMPT 120

    for i in range(len(date)):
        lout = lout + "'" + date[i] + "'" + "," + ",".join(str(k) for k in lfreq_ran[i]) + "," + str(avg_paid[i]) + "\n"
        
    return lout



## EXPORT THE STRINGS FROM THE "append_1_draw_to_output_list" FUNCTION AS A CSV FILE
def write_list_of_output_lines_to_file(lout, file_name):

##    PROVIDED. CMPT 120

    fileRef = open(file_name,"w") # opening file to be written
    for line in lout:
        fileRef.write(line)
                                    
    fileRef.close()
    
    return



## PRINTS OUT THE STATS FOR THE DRAWS
def main():
    print ("\nPlease confirm the output file name for your selected data")
    print ("If there is a file with this name in the folder, this new file will substitute the previous one")
    print ("Please add '.csv' at the end of the file name\n")

    ## ASK USER FOR AN OUTPUT FILE NAME
    file_name = input("Type x for OUTPUT file name 'OUT_results3.csv', or a new file name ==> ")

    if file_name == "x":
        file_name = "OUT_results3.csv"
    
    show_details_of_each_draw(receive_all_data[0], receive_all_data[1], receive_all_data[2], receive_all_data[3])
    print ("\nTRACE: Here is the output saved to the file =====>")
    print ("\n" + prepare_to_output)
    write_list_of_output_lines_to_file(prepare_to_output, file_name)
    print ("=========================== STATS =========================== ")
    print ("Draws processed: " + str(len(receive_all_data[0])))
    print ("\n" + receive_find_max_jackpot)
    print (receive_max_won)
    print("\nNumber of times each number was drawn")
    print (receive_count_each_number)
    print("\nNumber of numbers in each range - all selected draws considered")
    print("Ranges: (0,10], (10, 20], (20, 30], (30, 40], (40, 50]")
    print (receive_number_range)
    print ("\nSix most frequently drawn numbers")
    print (receive_frequent_numbers)
    turtle_graph(receive_number_range)
    
    return




## WHEN THE USER DOESN'T CHOOSE TO END THE PROGRAM
## DO ALL THE FOLLOWING REPEATEDLY
while end == False:

    ## FIRST, ASK THE USER TO INPUT THEIR OPTION OF "ALL", "SEL", OR "END"
    start = starthere(ask_user_for_input())


    ## IF THE USER CHOOSES TO PROCESS "ALL" OR "SELECTEED" DRAWS
    ## CALL THE FOLLOWING FUNCTIONS
    if start == "all_data" or start == "sel":
        receive_all_data = convert_lall_to_separate_lists(start)
        receive_all_data
        receive_find_max_jackpot = find_max_jackpot(receive_all_data[2], receive_all_data[0])
        receive_average_won = calculate_average_won(receive_all_data[2], receive_all_data[3])
        receive_max_won = (find_max_won(receive_average_won, receive_all_data[0]))
        receive_count_each_number = count_each_number_drawn(receive_all_data[1])
        receive_number_range = (range_for_all_draws(receive_all_data[1]))        
        receive_range_for_each_draw = range_for_each_draw(receive_all_data[1])
        receive_frequent_numbers = frequently_drawn_numbers()
        prepare_to_output = append_1_draw_to_output_list(receive_all_data[0], receive_range_for_each_draw, receive_average_won)


        main()


    ## IF THE USER TYPES IN INVALID OPTION, THEN KEEP ASKING USER UNTIL THEY TYPE IT RIGHT
    elif start == "ask_again":
        
        start = starthere(ask_user_for_input())

        ## ONCE THE USER TYPES IN A VALID OPTION
        ## CALL THE FOLLOWING FUNCTIONS
        if start == "all_data" or start == "sel":
            receive_all_data = convert_lall_to_separate_lists(start)
            receive_all_data
            receive_find_max_jackpot = find_max_jackpot(receive_all_data[2], receive_all_data[0])
            receive_average_won = calculate_average_won(receive_all_data[2], receive_all_data[3])
            receive_max_won = (find_max_won(receive_average_won, receive_all_data[0]))
            receive_count_each_number = count_each_number_drawn(receive_all_data[1])
            receive_range = (range_for_all_draws(receive_all_data[1]))
            receive_range_for_each_draw = range_for_each_draw(receive_all_data[1])
            receive_frequent_numbers = frequently_drawn_numbers()
            prepare_to_output = append_1_draw_to_output_list(receive_all_data[0], receive_range_for_each_draw, receive_average_won)


            main()












