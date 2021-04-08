from logging import Logger
from .model import Keyword as Keyword, Launch as Launch, LogMessage as LogMessage, Suite as Suite, Test as Test
from .service import RobotService as RobotService
from .variables import Variables as Variables
from typing import Any, Dict, List, Optional, Text, Union

logger: Logger

class listener:
    _items: List = ...
    ROBOT_LISTENER_API_VERSION: int = ...
    def __init__(self) -> None: ...
    def _build_msg_struct(self, message: Dict) -> LogMessage: ...
    def _finish_current_item(self) -> Union[Keyword, Launch, Suite, Test]: ...
    @property
    def current_item(self) -> Optional[Union[Keyword, Launch, Suite, Test]]: ...
    def log_message(self, message: Dict) -> None: ...
    def log_message_with_image(self, msg: Dict, image: Text) -> None: ...
    @property
    def parent_id(self) -> Optional[Text]: ...
    @property
    def service(self) -> RobotService: ...
    @property
    def variables(self) -> Variables: ...
    def start_launch(self, attributes: Dict, ts: Optional[Any] = None) -> None: ...
    def start_suite(self, name: Text, attributes: Dict, ts: Optional[Any] = None) -> None: ...
    def end_suite(self, _: Optional[Text], attributes: Dict, ts: Optional[Any] = None) -> None: ...
    def start_test(self, name: Text, attributes: Dict, ts: Optional[Any] = None) -> None: ...
    def end_test(self, _: Optional[Text], attributes: Dict, ts: Optional[Any] = None) -> None: ...
    def start_keyword(self, name: Text, attributes: Dict, ts: Optional[Any] = None) -> None: ...
    def end_keyword(self, _: Optional[Text], attributes: Dict, ts: Optional[Any] = None) -> None: ...
