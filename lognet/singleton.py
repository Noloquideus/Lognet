class SingletonLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonLogger, cls).__new__(cls)
            cls._instance.__init__(*args, **kwargs)
        return cls._instance