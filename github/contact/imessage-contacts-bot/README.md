# imessage-contacts-bot

### Basics:
**Input:** feed this bot an excel file with a list of people and phone numbers. 
<br/>**Result:** bot will add every person to your contact book (only if they do not exist already) and send desired message (as specified in excel file) to that person.


### Input Excel File
... it should look like this

| Last Name   | First Name  | Phone Num   | Contact type| Status      | Response    | Message     | 
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| ...         | ...         | ...         | ...         | NONE        | ...         | ...         |

- Last Name: put desired last name of contact
- First Name: put desired first name of contact
- Phone Num: put desired phone number of contact
- Contact type: this column must be here BUT it can be empty
- Status: Has a message already been sent? if the content in the column is anything besides NONE, a message will NOT be sent to this number
- Response: this column must be here BUT it can be empty
- Message: The message that will be sent to the phone number

### To Run
*of course this only runs on macos*
<br/>
1. download script
2. open excel file
3. double click script
4. "script editor" should open
5. press play button in top corner

