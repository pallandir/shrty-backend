import logging


class CustomLogger:
    # local loggers cache
    _loggers = {}

    def __init__(self, module_name: str, log_level: str = "INFO") -> None:
        if module_name in self._loggers:
            self.app_logger = self._loggers[module_name]
            return
        self.app_logger = logging.getLogger(module_name)
        self.app_logger.setLevel(log_level)

        if not self.app_logger.hasHandlers():
            handler = logging.StreamHandler()
            handler.setFormatter(
                logging.Formatter(
                    "| LEVEL : %(levelname)s | MODULE : %(name)s AT : %(asctime)s | MESSAGE : %(message)s"
                )
            )
            self.app_logger.addHandler(handler)

        self._loggers[module_name] = self.app_logger

    def get_logger(self):
        return self.app_logger
