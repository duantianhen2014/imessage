on run {targetPhone, message}
	tell application "Messages"
		set targetService to 1st account whose service type = iMessage
		set babe to participant targetPhone of targetService
		send message to babe
	end tell
end run