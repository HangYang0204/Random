## Using CDO API to send out email

CDO(Collaboration Data Objects) is an API with __Windows__. The library allows developers to access the Global Address List and other server objects, in addition to the contents of mailboxes and public folders(wiki).\
Specially we are talking about CDOSYS which is available on Windows 2000 and onwards by installing the SMTP service in Internet Information Server (IIS).


## Using it in VBA to get a qucik review of its functionality

To start, you need to add the reference: __Tools->References-> Microsoft CDO for Windows 2000 Library__ (this basically just included CDOSYS.dll from Windows)
Create a module and then type the following code:
```VBA
Public Sub SendSimpleCDOMail()

    Dim mail    As CDO.Message
    Dim config  As CDO.Configuration
    
    Set mail = CreateObject("CDO.Message")
    Set config = CreateObject("CDO.Configuration")
    
    config.Fields(cdoSendUsingMethod).Value = cdoSendUsingPort
    config.Fields(cdoSMTPServer).Value = "000.00.0.00"
    config.Fields(cdoSMTPServerPort).Value = 25
    'Using default credential 
    'config.Fields(cdoSMTPAuthenticate).Value = cdoNTLM

    config.Fields(cdoSMTPAuthenticate).Value = cdoBasic
    config.Fields(cdoSendUserName).Value = "Hang.Yang@Email"
    config.Fields(cdoSendPassword).Value = "PassSord"

    config.Fields.Update
    
    Set mail.Configuration = config
    
    With mail
        .To = "Receiver@Email"
        .From = "Sender@Email"
        .Subject = "First email with CDO"
        .TextBody = "This is the body of the first plain text email with CDO."
        
        .Send
    End With
    
    Set config = Nothing
    Set mail = Nothing
    
End Sub
```
To use the service, you must provide valid server address. For authentication, If your application is used within a Windows Domain with Active Directory and the user is authenticated in the domain, you can use NTLM authentication(Note that the email server must have configed to allow it)

## Using VC++ 
TODO
