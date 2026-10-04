

from operator import ne
playername=input("What is your name")

print(playername + ", you want to meet the Prof ???")
print("I am his assistant")
print("First you have to pass this quiz")
print(); 






answer = input("ok, tell me tell me how to spell 'python'?\n")



if answer.lower() == "pneumonoultramicroscopicsilicovolcanoconiosis":
    print("CORRECT good job, you might get it but  but let us not get to cocky ")
else:
    print(" OMG your chances of getting it are very low")  
print()

answer = input("Give me an 8 letter English word with at least 3 vowels\n")
if len(answer) == 8:
    print("Your word has 8 letters ...")
    count_a = answer.count('a')
    count_e = answer.count('e')
    count_i = answer.count('i')
    count_o = answer.count('o')
    count_u = answer.count('u')
    
    count_vowels = count_a+count_e+count_i+count_o+count_u 
    if count_vowels > 3:
        print("Oof ... you gave me more than 3 vowels")
        print("You are wasting my time, I needed only 3.")
    elif count_vowels < 3:
        print("that had less than 3 vowels")
        print("You tried to act smart, but I caught you.")
    else:
        print("What exactly 3 vowels ")
        print("You are not motivated, you are not putting any extra effort")
        print("You are not even trying to impress the Prof.")
else:
    print("You seem to be a disaster.")
    print("That word did not even have 8 letters.")

print()
sentence = input("ok, tell me a sentence ending in ' best prof of all time.' (no question please)\n")

if sentence.endswith('intelligent assistant'):
    print("Haven't you learnt about punctuations?")
elif sentence.endswith('intelligent assistant.'):
    len_first = sentence.find(' ')
    if len_first < 5:
        print("The first word in the sentence is too short.")
else:
    print("I really think you will make the prof. furious.")
    print("Please get the next one right it can lighten my mood .")






print()   
print("Ok, pick your preferred appointment time for next Monday(A/B/C/D)")
print("A. 8 mins past midnight", "B. 16 mins before sunrise", sep='\t'); 
print("C. 24 mins before noon", "D. 48 mins after sunset", sep='\t');
appointment = input('Select your slot (A/B/C/D)\n')


print("E. at midnight on top of everest ", "F. 16 mins before midnight", sep='\t'); 
print("G. 24 mins before lunch (lunch = 12:30)", "H. 48 mins after midnight", sep='\t');
appointment = input('Select your slot (E/F/G/H)\n')

if appointment == 'A':
    print("Careful, Prof may be already in a appointment.")
elif appointment == 'B':
    print("Warning, Prof. may be diving.")
elif appointment == 'C':
    print("Beware, Prof. may be watching tv.")
else:
    print("Caution, Prof. may be in a call.")


if appointment == 'E':
    print("Careful, Prof may be sleeping.")
elif appointment == 'F':
    print("Warning, Prof. may be jogging.")
elif appointment == 'G':
    print("Beware, Prof. may be swimming.")
else:
    print("Caution, Prof. may be dreaminng.")

print()
print("Good luck for your appointment, bye for now!")




       