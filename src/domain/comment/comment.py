from dataclasses import dataclass, field

from domain.comment.comment_id import CommentID
from domain.comment.text import Text
from domain.task.task_id import TaskID


@dataclass(frozen=True)
class Comment:
    """コメント"""

    id: CommentID
    task_id: TaskID
    text: Text = field(compare=False)
