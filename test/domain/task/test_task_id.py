class TestTaskID:
    """TaskIDのテスト"""

    def test___repr__(self):
        from domain.task.task_id import TaskID

        task_id: TaskID = TaskID("sample")
        result: str = task_id.__repr__()
        module_name: str = task_id.__module__
        qualified_name: str = task_id.__class__.__qualname__
        assert result == f"{module_name}.{qualified_name}('sample')"
