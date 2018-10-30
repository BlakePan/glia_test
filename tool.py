import sys
import traceback


def exception_parser():
  exc_type, err_val, tb = sys.exc_info()
  f = tb.tb_frame
  error_msg_list = list()
  for line in traceback.TracebackException(type(err_val), err_val, tb, limit=None).format(chain=True):
    error_msg_list.append(line)
  line_number = tb.tb_lineno
  filename = f.f_code.co_filename
  return filename, line_number, err_val, error_msg_list
