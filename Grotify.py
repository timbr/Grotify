import Skype4Py
import sys
import time


mobilenumber = "tim.browning3"

# This variable will get its actual value in OnCall handler
CallStatus = 0

# Here we define a set of call statuses that indicate a call has been either aborted or finished
CallIsFinished = set ([Skype4Py.clsFailed, Skype4Py.clsFinished, Skype4Py.clsMissed,
    Skype4Py.clsRefused, Skype4Py.clsBusy, Skype4Py.clsCancelled]);


def AttachmentStatusText(status):
    return skype.Convert.AttachmentStatusToText(status)


def CallStatusText(status):
    return skype.Convert.CallStatusToText(status)


WavFile = 'send.wav'


# This handler is fired when status of Call object has changed
def OnCall(call, status):
    global CallStatus
    global WavFile
    global OutFile
    CallStatus = status
    print 'Call status: ' + CallStatusText(status)

##    if (status == Skype4Py.clsEarlyMedia or status == Skype4Py.clsInProgress) and OutFile != '' :
##        print ' recording ' + OutFile
##        call.OutputDevice( Skype4Py.callIoDeviceTypeFile ,OutFile )
##        OutFile=''

    if status == Skype4Py.clsInProgress and WavFile != '' :
        print ' playing ' + WavFile
        call.InputDevice( Skype4Py.callIoDeviceTypeFile ,WavFile )


HasConnected = False

def OnInputStatusChanged(call, status):
    global HasConnected
    print 'InputStatusChanged: ',call.InputDevice(),call,status
    print ' inputdevice: ',call.InputDevice()
    # Hang up if finished
    if status == True:
        HasConnected = True
    if status == False and HasConnected == True:
        print ' play finished'
##        call.Finish()

# This handler is fired when Skype attatchment status changes
def OnAttach(status):
    print 'API attachment status: ' + AttachmentStatusText(status)
    if status == Skype4Py.apiAttachAvailable:
        skype.Attach()

# ----------------------------------------------------------------------------------------------------
# Fired on chat message status change.
# Statuses can be: 'UNKNOWN' 'SENDING' 'SENT' 'RECEIVED' 'READ'

def OnMessageStatus(Message, Status):
##    if Status == 'RECEIVED':
##        print(Message.FromDisplayName + ': ' + Message.Body);
##    if Status == 'SENT':
##        print('Myself: ' + Message.Body);

      if Status == 'RECEIVED':
          print(Message.FromDisplayName + ': ' + Message.Body);
##          print "will phone in 10 seconds"
##          time.sleep(10)
          global WavFile

          if Message.Body == '1':
              WavFile = 'The Laughing Policeman.wav'
              print "Calling mobile"
              skype.PlaceCall(Message.FromDisplayName)
          elif Message.Body == '2':
              WavFile = 'The Ugly Duckling.wav'
              print "Calling mobile"
              skype.PlaceCall(Message.FromDisplayName)
          elif Message.Body == '3':
              WavFile = 'Robin Hood.wav'
              print "Calling mobile"
              skype.PlaceCall(Message.FromDisplayName)
          elif Message.Body == '4':
              WavFile = 'The Hippopotamus Song.wav'
              print "Calling mobile"
              skype.PlaceCall(Message.FromDisplayName)
          elif Message.Body == '5':
              WavFile = 'butchers.wav'
              print "Calling mobile"
              skype.PlaceCall(Message.FromDisplayName)
          else:
              message="""Welcome to Grotify - inspired by a hungover afternoon
------------------------------
Songs available:

1: The Laughing Policeman
2: The Ugly Duckling
3: Robin Hood
4: The Hippopotamus Song
5: The Shankhill Butchers

Type the number to hear the song."""
              skype.CreateChatWith(Message.FromDisplayName).SendMessage(message)



skype = Skype4Py.Skype()
skype.OnAttachmentStatus = OnAttach
skype.OnCallStatus = OnCall
skype.OnCallInputStatusChanged = OnInputStatusChanged
skype.OnMessageStatus = OnMessageStatus

# Starting Skype if it's not running already..
if not skype.Client.IsRunning:
    print 'Starting Skype..'
    skype.Client.Start()

# Attatching to Skype..
print 'Connecting to Skype..'
skype.Attach()


# Loop until CallStatus gets one of "call terminated" values in OnCall handler
##while not CallStatus in CallIsFinished:
##    time.sleep(0.1)


# ----------------------------------------------------------------------------------------------------
# Looping until user types 'exit'
Cmd = '';
while not Cmd == 'exit':
    Cmd = raw_input('');