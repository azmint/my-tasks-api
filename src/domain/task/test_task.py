class TestTask:
    """Taskのテスト"""

    def test___eq__(self):
        """==でidのみが比較されているか"""
        from datetime import timedelta
        from domain.task.task import Task
        from domain.task.task_id import TaskID
        from domain.task.summary import Summary
        from domain.task.details import Details
        from domain.task.status import Status
        from domain.task.relations import Relations
        from domain.task.relations import Relation
        from domain.task.relations import Type
        from domain.task.initial_estimate import InitialEstimate

        task1: Task = Task(
            TaskID("sample_id"),
            Summary("sample_name1"),
            Details("sample_details1"),
            Status.OPEN,
            Relations([Relation(Type.PARENT, TaskID("parent_id1"))]),
            InitialEstimate(timedelta()),
        )
        task2: Task = Task(
            TaskID("sample_id"),
            Summary("sample_name2"),
            Details("sample_details2"),
            Status.RESOLVED,
            Relations([Relation(Type.PARENT, TaskID("parent_id2"))]),
            InitialEstimate(timedelta()),
        )
        assert task1 == task2

    def test___ne__(self):
        """==でidのみが比較されているか"""
        from datetime import timedelta
        from domain.task.task import Task
        from domain.task.task_id import TaskID
        from domain.task.summary import Summary
        from domain.task.details import Details
        from domain.task.status import Status
        from domain.task.relations import Relations
        from domain.task.relations import Relation
        from domain.task.relations import Type
        from domain.task.initial_estimate import InitialEstimate

        task1: Task = Task(
            TaskID("sample_id1"),
            Summary("sample_name"),
            Details("sample_details"),
            Status.OPEN,
            Relations([Relation(Type.PARENT, TaskID("parent_id"))]),
            InitialEstimate(timedelta()),
        )
        task2: Task = Task(
            TaskID("sample_id2"),
            Summary("sample_name"),
            Details("sample_details"),
            Status.OPEN,
            Relations([Relation(Type.PARENT, TaskID("parent_id"))]),
            InitialEstimate(timedelta()),
        )
        assert task1 != task2
