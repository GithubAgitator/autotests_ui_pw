import sys

import pytest
import random




@pytest.mark.flaky(reruns=2, reruns_delay=2)
@pytest.mark.xfail
def test_runs_1():
    assert random.choice([True, False])

@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=sys.platform.startswith("win32"))  # Перезапуск при выполнении условия
@pytest.mark.xfail
def test_rerun_with_condition():
    assert random.choice([True, False])