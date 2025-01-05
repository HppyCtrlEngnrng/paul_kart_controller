from abc import ABC, abstractmethod
from controller_input import ControllerInput
from controller_output import ControllerOutput

class ControllerBase(ABC):
    @abstractmethod
    def step(self, controller_input: ControllerInput, *args, **kwargs) -> ControllerOutput:
        pass
