set {lName, fName, pNum, status, pMessage} to getData()

repeat with i from 1 to count fName
	log item i of fName & " " & item i of lName
	delay 1
	if (item i of status = "NONE") then
		if (checkContactExist(item i of fName, item i of lName, item i of pNum) = false) then
			tell application "Contacts"
				set newContact to make new person with properties {first name:item i of fName, last name:item i of lName}
				tell newContact
					make new phone at end of phones with properties {label:"phone", value:item i of pNum}
				end tell
				save
			end tell
			tell application "Messages"
				set targetService to (1st account whose service type = iMessage)
				set targetPhone to item i of pNum
				set targetBuddy to participant targetPhone of targetService
				set payload to item i of pMessage
				send payload to targetBuddy
				
			end tell
		end if
	end if
end repeat

on checkContactExist(currentFName, currentLName, currentPNum)
	tell application "Contacts"
		return (exists (1st person whose first name is currentFName and last name is currentLName and value of phones contains currentPNum))
	end tell
end checkContactExist


on getData()
	set colA to {} --last name
	set colB to {} --first name
	set colC to {} --phone number
	set colD to {} --class
	set colE to {} --status
	set colF to {} --e
	set colG to {} --message
	
	tell application "Microsoft Excel"
		activate
		tell active sheet
			set lastRow to first row index of (get end (last cell of column 1) direction toward the top)
			repeat with i from 1 to lastRow
				set end of colA to (value of range ("A" & i))
				set end of colB to (value of range ("B" & i))
				set end of colC to (value of range ("C" & i))
				set end of colD to (value of range ("D" & i))
				set end of colE to (value of range ("E" & i))
				set end of colF to (value of range ("F" & i))
				set end of colG to (value of range ("G" & i))
			end repeat
		end tell
	end tell
	return {colA, colB, colC, colE, colG}
end getData
