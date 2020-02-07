import pexpect, sys, time
# This script can be used to repeatedly start and toss nethack games
# in order to get the character you want.
# by
# jblakey@gmail.com

############################# CONFIGURATION ################################

# Make sure these items are in the order that they normally appear
# in your inventory...
# The default order is Scrolls, Spellbooks, Potions, Rings, Wands, Tools
# DO NOT USE META CHARACTERS HERE...
wanted_objects = ["identify", "spellbook of charm", "magic marker"]

nethack_command = "nethack"
char_alignment = "n"
char_race = "h"
char_sex = "m"
char_class="w"
max_tries = 5000

########################## END CONFIGURATION ################################

def scum(wantedObjectsList):

    myWantedObjects = []

    # First, build the regex from the wantedObjectsList...
    # This is a little junky, and prone to breakage...
    # but so far, it works...
    big_regex = ""
    for thisItem in wantedObjectsList:
         big_regex += "(" + thisItem + ").+"

    myWantedObjects.append(big_regex)
    
    # And then append the (end) tag...
    myWantedObjects.append(r'\(end\)')

    # Add this in case we get that darn blindfold, and it kicks
    # us over to a 2 page inventory...
    myWantedObjects.append(r'\(1 of 2\)')

    n = pexpect.spawn(nethack_command)
    n.setecho(True)
    r = n.expect("Shall I pick")
    my_specs = "n" + char_class + char_race + char_sex + char_alignment + "y"
    n.send(my_specs)
    n.expect("Go bravely")
    n.send(' ')
    n.expect("welcome to")
    n.sendline("")

    # Send a few spaces in case we're standing on anything...
    n.send(' ')
    n.send(' ')
    n.send(' ')

    # Send the inventory command...
    n.send("i")

    match_index  = n.expect(myWantedObjects, timeout=1)

    n.send(' ')
    n.send(' ')
    n.send(' ')

    # Success, save the character...
    if match_index == 0:
        n.sendline("Sy")
        return True

    # Otherwise, toss this character...
    else:
        n.sendline("#quit")
        n.send('y')
        n.send('q')
        return False

def main():

    for i in range(1, max_tries):

        print("Run: " + str(i))
        success = scum(wanted_objects)

        if success:
            print("Your character has all the items you wanted, is saved and ready to go!")
            exit()
        else:
            continue

if __name__ == "__main__":
    main()
