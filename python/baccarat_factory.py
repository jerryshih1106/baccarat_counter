
from .method import LogicalCardCounting, HighLevelCounting
from .except_handler import MethodChooseError, except_decorator
ALGO_DICT = {"H": HighLevelCounting, 'L': LogicalCardCounting} 

class BaccaratFactory:
    def __init__(self, mode):
        self.mode = mode
        self._check_mode()
    
    @except_decorator
    def _check_mode(self):
        try:
            self.mode = "HighLevelCounting" if self.mode == "" else self.mode
            self.process = ALGO_DICT[self.mode]()
        except Exception as e:
            raise MethodChooseError(e)