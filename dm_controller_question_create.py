# Module Name      : dm_controller_question_create
# Module Purpose   : create a question
# Status           : Completed
# Parameters       : (question <question>)
# Returns          : Call to controller
#
# Module Author    : Lewis Francis C1826277
# Start Date       : 07/03/2020
# End Date         : 14/03/2020
# Hours Spent      : 1

import dmcontroller
def dm_controller_question_create("question", "create", question):
    try:
        dm_controller("question", "create", question)
        return True
    except:
        return False
        print:("dm_controller_question_create Error")
