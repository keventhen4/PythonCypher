from processScript import scriptTranscribe

scriptFile, compiledFile = "script.txt", "compiled.txt"
scriptTranscribe = scriptTranscribe(scriptFile, compiledFile)
scriptTranscribe.Compile()
scriptTranscribe.Close()


scriptFile = open(f"./{compiledFile}", "r")
exec(scriptFile.read())
scriptFile.close()