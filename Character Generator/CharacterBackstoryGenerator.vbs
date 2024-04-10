Set WshShell = CreateObject("WScript.Shell")

' Specify the relative path to the batch file
Dim batchFilePath
batchFilePath = ".\python\run.bat"

' Run the batch file headlessly
WshShell.Run Chr(34) & batchFilePath & Chr(34), 0, True

Set WshShell = Nothing