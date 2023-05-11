(* The below snippet sends the actual email & text.
It gets the email content, sms content, email id & phone as input
Please note the phone number should be PREFIXED BY COUNTRY CODE
*)

on sendTextEmail(emailContent, smsContent, email1, ph, name1)
	
	if email1 is not "" then
		tell application "Mail"
			set theMessage to make new outgoing message with properties {visible:true, subject:"Medley: Upcoming Role", content:emailContent}
			tell theMessage
				make new to recipient at end of to recipients with properties {name:name1, address:email1}
				set sender of theMessage to "tushar saurabh "
				send
			end tell
		end tell
	else
		tell application "Mail"
			set theMessage to make new outgoing message with properties {visible:true, subject:"Error Mail - Medley: Upcoming Role", content:name1}
			tell theMessage
				make new to recipient at end of to recipients with properties {name:"tushar saurabh ", address:"saurabh.tushar@gmail.com"}
				set sender of theMessage to "tushar saurabh "
				send
			end tell
		end tell
		
	end if
	
	if ph is not "" then
		tell application "Messages"
			send smsContent to buddy ph of service "SMS"
		end tell
	end if
	
end sendTextEmail
--#############################################################################################################################

(* Sets the SMS Content and Email Content
*)
on processRemind(meetingNumber, name1, role1, email1, ph, meetingDate)
	
	set emailContent to "Greetings Toastmaster " & name1 & ",

" & "Thanks for agreeing to play role of " & role1 & ".
Please be available for meeting by 2:45 PM to avoid last minute confusion. 

Thanks & Regards,
 Tushar Saurabh, 
 VPE-Medley 
 Phone: 805 602 4308"
	set smsContent to "Greetings!!" & name1 & ",Thanks for agreeing to play the role of " & role1 & ".Please be by 2:45 PM to avoid confusion."
	sendTextEmail(emailContent, smsContent, email1, ph, name1)
end processRemind
--#############################################################################################################################



on processInform(meetingNumber, name1, role1, email1, ph, meetingDate)
	
	set emailContent to "Greetings Toastmaster " & name1 & ",

" & "Medley needs your services for conducting its business.
 Please let me know, if you would be available for 

 Role: " & role1 & " on " & meetingDate & ".

Thanks & Regards,
 Tushar Saurabh, 
 VPE-Medley 
 Phone: 805 602 4308"
	set smsContent to "Greetings!!" & name1 & ",would you agree to play role of " & role1 & " on " & meetingDate
	sendTextEmail(emailContent, smsContent, email1, ph, name1)
end processInform

--The crux of the program. It loops through the record and gets individual data

on callInformRemind(callType, meetingData, meetingNumber)
	
	set meetingLongDate to |date| of meetingData's item 1
	set meetingDate to text 1 thru 10 of meetingLongDate
	
	repeat with counter_variable_name from 2 to count of meetingData
		set current_role to item counter_variable_name of meetingData
		set name1 to |name| of current_role
		set role1 to role of current_role
		set contact1 to contact of current_role
		set phone1 to phone of contact1
		set ph to "+91" & phone1
		set email1 to email of contact1
		
		if callType = "Inform" then
			processInform(meetingNumber, name1, role1, email1, ph, meetingDate)
		else
			processRemind(meetingNumber, name1, role1, email1, ph, meetingDate)
		end if
	end repeat
end callInformRemind

set meetingInput to display dialog "Enter Meeting Number" default answer "" buttons {"Inform", "Remind"} default button "Inform"
set informType to button returned of meetingInput
set meetingNumber to text returned of meetingInput

--Using JSON Helper, a third party tool to call GoogleSheet Web Api. ?number is the query string passed

tell application "JSON Helper"
	--Get UK police forces information	
	set meetingData to fetch JSON from "https://example.com/exec?number=" & meetingNumber
end tell

if meetingData's item 1 = "Meeting Not Found" then
	return "Meeting Not Found!"
else
	callInformRemind(informType, meetingData, meetingNumber)
end if



