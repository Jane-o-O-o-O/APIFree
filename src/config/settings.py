class Settings:
    def __init__(self, debug: bool = False, log_level: str = "INFO"):
        self.debug = debug
        self.log_level = log_level

    def __repr__(self):
        return f"Settings(debug={self.debug}, log_level='{self.log_level}')"