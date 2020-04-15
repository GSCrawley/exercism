import re

def abbreviate(words):
    return ''.join(re.findall(r"(?<![A-Z'])[A-Z]", words.upper()))

    return abbreviate(words)
    
print(abbreviate("Will This Work"))
print(abbreviate("Will It Even Work With A Super Duper Extra Long String?"))
print(abbreviate("WowItLooksLikeItEvenWorksWithASuperDuperExtraLongStringButIBetItWontReallyWorkVeryWellWithThisEdgeCaseOfAStringWithNoSpaces"))