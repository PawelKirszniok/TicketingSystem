from sqlalchemy.exc import SQLAlchemyError

def exception_handler(function):
    """
    this decorator add exception handling to any method of the DatabaseService class it is applied to.
    """
    def wrapper(self, *args, **kwargs):

        try:
            result = function(self, *args, **kwargs)
        except SQLAlchemyError:
            self.session.rollback()
            return None

        return result

    return wrapper
