import logging


class LogGen:
    @staticmethod
    def loggen():
        log_file_path = r"D:\Ailaysa_automation\trail1st\logs\automation.log"

        # Create logger and set the log level
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # Create a handler for writing log messages to the file (append mode)
        file_handler = logging.FileHandler(log_file_path, mode='a')

        # Define log message format
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        file_handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(file_handler)

        return logger
