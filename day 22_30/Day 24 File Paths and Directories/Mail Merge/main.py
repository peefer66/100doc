#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


#day 22_30\Day 24 File Paths and Directories\Mail Merge\Input\Letters\starting_letter.txt

# Create a list of all the invitees
# invitee_list = []
PLACEHOLDER = '[name]'
with open(r"C:\Users\pfiel\Documents\Python\100doc\day 22_30\Day 24 File Paths and Directories\Mail Merge\Input\Names\invited_names.txt") as invitees:
    # create list of names to invite
    invitee_list = [name.strip() for name in invitees.readlines()]

# cahnge the invite letter template to each name
for name in invitee_list:
    with open(r'C:\Users\pfiel\Documents\Python\100doc\day 22_30\Day 24 File Paths and Directories\Mail Merge\Input\Letters\starting_letter.txt') as invite_letter:
        letter = invite_letter.read()
        #Repalce the PLACEHOLDER with the invitee name
        letter = letter.replace(PLACEHOLDER, name)
        # append .txt
        letter_to_save = name + '.txt'
        # open/create invite to send using the mode='w'
        with open(r'C:\Users\pfiel\Documents\Python\100doc\day 22_30\Day 24 File Paths and Directories\Mail Merge\Output\ReadyToSend\\' + letter_to_save, mode='w') as invite_to_send:
            invite_to_send.write(letter)
            
        
