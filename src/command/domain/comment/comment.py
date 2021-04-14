from dataclasses import dataclass, field

from command.domain.comment.comment_id import CommentID
from command.domain.comment.text import Text
from command.domain.task.task_id import TaskID


@dataclass(frozen=True)
class Comment:
    """コメント"""

    id: CommentID
    task_id: TaskID
    text: Text = field(compare=False)
