from time import perf_counter


class Stopwatch:
    def __init__(self):
        self.__step_count = 0
        self.__start_time = 0
        self.__end_time = 0
        self.__break_time = 0

    def start(self) -> None:
        self.__start_time = perf_counter()

    def timeout(self) -> None:
        self.__break_time = perf_counter()

    def resume(self) -> None:
        if self.__break_time != 0:
            self.__start_time += perf_counter() - self.__break_time
        self.__break_time = 0

    def stop(self) -> None:
        if self.__start_time == 0:
            self.__end_time = 0
        else:
            self.__end_time = perf_counter()

    def time_per_second(self) -> float:
        if self.__start_time == 0:
            return 0
        if self.__end_time == 0:
            return perf_counter()-self.__start_time
        else:
            return self.__end_time - self.__start_time
