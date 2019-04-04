import notify2
import sys

notify2.init('CryptoCut')

#0 > UpdateSettingNotif
#1 > NotUpdateSettingNotif
#2 > DASHNotif
#3 > ETHNotif
#4 > BTCNotif
#5 > LTCNotif

x=int(sys.argv[0])


def ShowNotify(x):
	UpdateSettingNotif = notify2.Notification("CryptoCut Settings","Changes applied successfully","notification-message-im")
	NotUpdateSettingNotif = notify2.Notification("CryptoCut Settings","Applying Changes Faild","notification-message-im")
	DASHNotif = notify2.Notification("CryptoCut Donate","Dash Address Copied Successfully","notification-message-im")
	ETHNotif = notify2.Notification("CryptoCut Donate","Ethereum Address Copied Successfully","notification-message-im")
	BTCNotif = notify2.Notification("CryptoCut Donate","Bitcoin Address Copied Successfully","notification-message-im")
	LTCNotif = notify2.Notification("CryptoCut Donate","Litecoin Address Copied Successfully","notification-message-im")
	if (0==x):
		UpdateSettingNotif.show()
	if (1==x):
		NotUpdateSettingNotif.show()
	if (2==x):
		DASHNotif.show()
	if (3==x):
		ETHNotif.show()
	if (4==x):
		BTCNotif.show()
	if (5==x):
		LTCNotif.show()
