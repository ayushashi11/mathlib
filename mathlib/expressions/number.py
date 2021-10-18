class __AnyNumber:
    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return True
        return False

ANYNUMBER = __AnyNumber()
