import cypherMap



class scriptTranscribe():
    def __init__(self, scriptFile, compileFile):
        self.Wipe(compileFile)

        self.scriptFile = scriptFile #Script file to read line by line in self.Compile()
        self.compileFile = open(f"./{compileFile}", "a") #File to write/append to

        self.compiledLine = "" #Line to write/append to the compiled code
        self.boundTo = None #Variable for checking if working with strings and similar


    def Compile(self): #Loops through every character of every line in script file, performs checks, compiles to compiled code file
        with open(f'./{self.scriptFile}') as script:
            for line in script:
                for character in line:
                    self.BoundCheck(character) #BoundCheck to check if working with bounded values
                    self.Map(character)
                self.compileFile.write(self.compiledLine)
                self.compiledLine = ""

    def BoundCheck(self, character):
        if self.SearchZhEn(character, "Characters"):
            if (cypherMap.zhEn["Characters"][character] in cypherMap.bounds or character in cypherMap.bounds):
                if self.boundTo == None:
                    if cypherMap.zhEn["Characters"][character] in [cypherMap.bounds[0], cypherMap.bounds[1]]:
                        self.boundTo = cypherMap.zhEn["Characters"][character]
                    elif character == cypherMap.bounds[2]:
                        self.boundTo = cypherMap.bounds[2]
                elif (cypherMap.zhEn["Characters"][character] == self.boundTo or character == self.boundTo):
                    self.boundTo = None

    def Map(self, character):
        try:
            if self.boundTo == None:
                print(self.boundTo)
                self.compiledLine += self.SearchZhEn(character) #
            else:
                if (character != self.boundTo and not self.SearchZhEn(character, "Characters")):
                    self.compiledLine += character
                else:
                    self.compiledLine += self.SearchZhEn(character)
        
        except: raise NotImplementedError(f"Character was not found in mapping and may not be implemented currently.\nCharacter: {character}")

    @staticmethod
    def SearchZhEn(self, character, type=False):
        if type:
            if character in cypherMap.zhEn[type]:
                return cypherMap.zhEn[type][character]
        else:
            for types in cypherMap.zhEn:
                if character in types:
                    return cypherMap.zhEn[types][character]
        return False


    def Wipe(self, compileFile): #wipes file by overwriting with blank string
        with open(f"./{compileFile}", "w") as wipedCompileFile:
            wipedCompileFile.write("")

    def Close(self): #close files
        #self.scriptFile.close()
        self.compileFile.close()

