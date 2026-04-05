import sys
# from src.logger import logging  # Your central logger

def error_message_detail(error, error_detail: sys):
    """
    Create a detailed error message with:
    - file name
    - line number
    - error message
    """
    _, _, exc_tb = error_detail.exc_info()  # get traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # correct attribute for file name

    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # call parent Exception constructor
        self.error_message = error_message_detail(error_message, error_detail)  # store detailed message

    def __str__(self):
        return self.error_message  # what print(CustomException) will show
    

    