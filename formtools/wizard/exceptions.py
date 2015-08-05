class DoneStepError(Exception):
    pass

class DoneStepValidationError(DoneStepError):
    def __init__(self, step_errors):
        """
            step_errors is a dict where keys == step, values == list of ValidationErrors
        """
        self.step_errors = step_errors

class RepeatDoneStepError(DoneStepError):
    def __init__(self, response):
        self.response = response