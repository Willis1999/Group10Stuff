# Module Name      : dm_controller_question_read
# Module Purpose   : read qustion
# Status           : Completed
# Parameters       : ("read")
# Returns          : returns call to dm_controller
#
# Module Author    : Lewis Francis C1826277
# Start Date       : 08/03/2020
# End Date         : 15/03/2020
# Hours Spent      : 1
import dm_controller
def dm_controller_question_read("question", "read", question):
    try:
        dm_controller("question", "read", question)
        return True
    except:
        return False
        print:("dm_controller_question_read Error")
