from Hate_Speech.logger import logging
from Hate_Speech.exception import CustomException
import sys

# logging.info("Wellcome to my project")

try:
    a = 7/0
    
except Exception as e:
    raise CustomException(e, sys) from e
