#------------------------------------------------------------------------------
# Copyright (c) 2019, Infinite Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------

import notify2


notify2.init("CryptoCut")
DoneNofification = notify2.Notification("Done","Encrypted successfully","notification-message-info")
DoneNofification.show()
