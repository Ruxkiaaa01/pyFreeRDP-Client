#
# 	This is not a working client yet, just a work in progress, trying to figure it out
#
# 	useful links
# 		- https://stackoverflow.com/questions/21210283/rdp-script-in-python
# 		- https://github.com/FreeRDP/FreeRDP/issues/3201#issuecomment-207111329
# 		- https://github.com/FreeRDP/FreeRDP/blob/master/client/Sample/tf_freerdp.c
# 		- https://github.com/FreeRDP/FreeRDP/wiki/PreBuilds
# 		- https://docs.python.org/3/library/ctypes.html
#
#
#

from ctypes import *

freerdpc = cdll.LoadLibrary("/usr/local/Cellar/freerdp/2.4.0/lib/libfreerdp-client2.dylib")
ep = None
contxt = freerdpc.freerdp_client_context_new(ep)

# status = freerdpc.freerdp_client_settings_parse_command_line(contxt, None, None, False)
# rc = freerdpc.freerdp_client_settings_command_line_status_print(contxt, status, None, None)

freerdpc.freerdp_client_start(contxt)
freerdpc.freerdp_client_stop(contxt)
freerdpc.freerdp_client_context_free(contxt)
