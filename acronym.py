import re

def abbreviate(words):
    return ''.join(re.findall(r"(?<![A-Z'])[A-Z]", words.upper()))

    return abbreviate(words)

#Good test case 
print(abbreviate("Will This Work"))
#Not-So-Great test case
print(abbreviate("Will It Even Work With A Super Duper Extra Long String?"))
#Edge-y Test Case
print(abbreviate("WowItLooksLikeItEvenWorksWithASuperDuperExtraLongStringButIBetItWontReallyWorkVeryWellWithThisEdgeCaseOfAStringWithNoSpaces"))
print(abbreviate("This Is Cool"))
print(abbreviate("Oh Really? What's so cool about it?"))
print(abbreviate("It'sAFunExerciseDudeLightenUp"))