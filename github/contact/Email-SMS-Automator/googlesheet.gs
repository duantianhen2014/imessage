function doGet(e) {
  
  var meetingNumber = e.parameters.number
  Logger.log(meetingNumber)
  var json = returnMeetingDataAsJSON(meetingNumber);
    
  return ContentService.createTextOutput(JSON.stringify(json))
    .setMimeType(ContentService.MimeType.JSON);

}

function testFunction(){
  returnMeetingDataAsJSON(360);
}

function returnMeetingDataAsJSON(meetingNumber) {
  var spreadSheet = SpreadsheetApp.openById("google-sheet-id");
  
  var agendaSheet = spreadSheet.getSheetByName("Jan to Dec 2016 Agenda");
  var memberContactSheet = spreadSheet.getSheetByName("Member Contacts");
  
  var jsonArray = [];
  var agendaRow = 4;
  var found = false;
  var name = "";
  var role = "";
  var phoneemail = "";
  var agendaValues = agendaSheet.getRange(4,1,agendaSheet.getLastRow(),agendaSheet.getLastColumn()).getValues();
  var tempCol = 0
  for (var i = 0; i < agendaValues.length; i++) {
    
    for (var j = 0; j < agendaValues[i].length;j++){
      if ((agendaValues[i][j] == meetingNumber) && !(found)){
        found = true;
        tempCol = j;
      }
    }
    if (found) {
      var roleDetails = {};
      if (agendaValues[i][tempCol] != "" && i != 0){
        if (i == 1){
          roleDetails["date"] = agendaValues[i][tempCol];
          jsonArray.push(roleDetails);
        } else {
        roleDetails["name"] = agendaValues[i][tempCol];
        roleDetails["role"] = agendaValues[i][0];
        roleDetails["contact"] = getPhoneNumberEmailId(agendaValues[i][tempCol],memberContactSheet);
        jsonArray.push(roleDetails);
        }
      }
      
    } else {
      jsonArray.push("Meeting Not Found");
      return jsonArray;
    }
      
  }
  Logger.log(jsonArray);
  return jsonArray;
}

function getPhoneNumberEmailId(name,memberContactSheet){
  var memberContactValues = memberContactSheet.getRange(2,3,100,3).getValues();
  var emailPhone = {};
  for (var i = 0; i<memberContactValues.length;i++){
    if (memberContactValues[i][0] == name){
      emailPhone["Phone"] = String(memberContactValues[i][2]);
      emailPhone["email"] = memberContactValues[i][1];
      return emailPhone;
    }
  }
  
}
