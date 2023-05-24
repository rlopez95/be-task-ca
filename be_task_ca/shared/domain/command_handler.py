from abc import ABC, abstractmethod

from be_task_ca.shared.domain.command import Command
from be_task_ca.shared.domain.command_response import CommandResponse


class CommandHandler(ABC):
    @abstractmethod
    def process(self, command: Command) -> CommandResponse:
        pass
