import time


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        return False


class Dummy:
    def __enter__(self):
        return 0

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class Suppressor:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True  # nunca deja salir la excepción


class SpySuppressor(Suppressor):
    def __init__(self):
        self.args = None

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.args = (exc_type, exc_val, exc_tb)
        return True


class NoSuppress:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False  # deja propagar
