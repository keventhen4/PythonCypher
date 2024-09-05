import cypherMap

compileFile = open("./compiled.txt", "w")
compileFile.write("")
compileFile.close()

"""
compileFile = open("./compiled.txt", "a")
compileFile.write("print('hello world')\n")
compileFile.write("print('haurhaur')")
compileFile.close()
"""

compileFile = open("./compiled.txt", "a")
compileLine = ""
boundTo = None
bounds = ['"', "'", "~"]
scriptFile = "script.txt"


def BoundCheck(character):
    global boundTo, bounds
    if character in cypherMap.zhEn and (cypherMap.zhEn[character] in bounds or character in bounds):
        if boundTo == None:
            if cypherMap.zhEn[character] == bounds[0] or cypherMap.zhEn[character] == bounds[1]:
                boundTo = cypherMap.zhEn[character]
            elif character == bounds[2]:
                boundTo = bounds[2]
        else:
            boundTo = None if (cypherMap.zhEn[character] == boundTo or character == boundTo) else boundTo

def Transcribe(character):
    global compileLine
    if boundTo != None:
        if (character != boundTo and character not in cypherMap.zhEn): compileLine += character
        else: compileLine += cypherMap.zhEn[character]
    else: compileLine += cypherMap.zhEn[character] #


with open(f'./{scriptFile}') as script:
    for line in script:
        for character in line:
            BoundCheck(character)
            Transcribe(character)
        compileFile.write(compileLine)
        compileLine = ""


#script = scriptFile.readlines()
compileFile.close()


compileFile = open("./compiled.txt", "r")
script = compileFile.readlines()
for line in script:
    exec(line)
compileFile.close()
