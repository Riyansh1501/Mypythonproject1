from operator import ne
playername=input("What is your name")

print(playername + ", you want to meet the Prof ???")
print("I am his assistant")
print("First you have to pass this quiz")
print(); 






answer = input("ok, tell me tell me how to spell 'python'?\n")



if answer.lower() == "python":
    print("CORRECT good job, you might meet him but let us not get to cocky ")
else:
    print(" OMG your chances of meeting the Prof. are very low")  
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
sentence = input("ok, tell me a sentence ending in 'intelligent assistant' (no question please)\n")

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


print("E.  on top of everest ", "F. on my desk", sep='\t'); 
print("G. at my house over  ", "H. on a football pitch", sep='\t');
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



print ("a few days later")  

print ("hello good to see you again")
print("ya you too")
print()
print()
input("the prof is waiting for you do you want to mee t him now yes or no")
answer = input("Select your slot (yes / no)\n")

if answer==yes:
    print ("come with me")
else:
    print ("get out of here")


print ("doors open")

print()
print()


print ("hello..mm") (playername + ", how are you doing sorry i took you early the option you took i was busy")

print ("it is ok")

print ("I want the english Cambridge diploma")

print ("ok i will get it for you but you have to answer a few questions")

print("your lucky it will be the same questions the assistamt asked you before")

print ("it will be a little bit different but you will get it")

print ("ok i will try my best")


answer = input("ok, tell me tell me how to spell 'pneumonoultramicroscopicsilicovolcanoconiosis'?\n")



if answer.lower() == "pneumonoultramicroscopicsilicovolcanoconiosis":
    print("CORRECT good job, you might get it but  but let us not get to cocky ")
else:
    print(" OMG your chances of getting it are very low")  
print()

answer = input("Give me an 10 letter English word with at least 3 vowels\n")
if len(answer) == 10:
    print("Your word has 10 letters ...")
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
        print("You are not even trying to get it.")
        print("at least you got it correct that is what matters")
else:
    print("You seem to be a disaster.")
    print("That word did not even have 10 letters.")

print()
sentence = input("ok, tell me a sentence ending in ' best prof of all time.' (no question please)\n")

if sentence.endswith(' best prof of all time'):
    print("Haven't you learnt about punctuations?")
elif sentence.endswith('best prof of all time.'):
    len_first = sentence.find(' ')
    if len_first == 10:
        print("The first word in the sentence is too short.")
        print("But you got the ending correct that is what matters")
else:
    print("I really think you will not get it if you continue like this.")
    print("Please get the next one right it can lighten my mood .")

    print ("last question")
    print()
    print()

answer = input("ok, tell me the past tense of 'go'?\n")
if answer.lower() == "went":
  print("Correct! 🎉")
else:
 print("Incorrect. The answer is 'went'.")



 print ("after a few days you get the diploma")

 print ("good job you got the diploma and you are now a certified Cambridge English Diploma holder")
print ("goodbye and take care")