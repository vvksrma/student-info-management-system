import io
import sys
from contextlib import redirect_stdout
from project import main, create, update, delete, view


def test_create():
    # Test data
    data = []
    count = 0

    # Simulate user input
    inputs = iter(["John Doe", "101", "10-A"])

    def mock_input(prompt):
        return next(inputs)

    original_input = __builtins__.input
    __builtins__.input = mock_input

    try:
        # Capture output
        output = io.StringIO()
        with redirect_stdout(output):
            data, count = create(data, count)

        # Expected result
        expected_data = [{"ID": 1, "Name": "John Doe", "Roll No": "101", "Class": "10-A"}]

        assert data == expected_data, f"Expected {expected_data}, but got {data}"
        assert count == 1, f"Expected count to be 1, but got {count}"

        print("test_create passed.")

    finally:
        __builtins__.input = original_input


def test_view():
    # Test data
    data = [{"ID": 1, "Name": "John Doe", "Roll No": "101", "Class": "10-A"}]

    # Capture output
    output = io.StringIO()
    with redirect_stdout(output):
        view(data)

    # Check the output
    assert "John Doe" in output.getvalue(), "Name 'John Doe' not found in view output"
    assert "101" in output.getvalue(), "Roll No '101' not found in view output"
    assert "10-A" in output.getvalue(), "Class '10-A' not found in view output"

    print("test_view passed.")


def test_update():
    # Test data
    data = [{"ID": 1, "Name": "John Doe", "Roll No": "101", "Class": "10-A"}]

    # Simulate user input
    inputs = iter(["1", "Jane Doe", "102", "11-B"])

    def mock_input(prompt):
        return next(inputs)

    original_input = __builtins__.input
    __builtins__.input = mock_input

    try:
        # Capture output
        output = io.StringIO()
        with redirect_stdout(output):
            data = update(data)

        # Expected result
        expected_data = [{"ID": 1, "Name": "Jane Doe", "Roll No": "102", "Class": "11-B"}]

        assert data == expected_data, f"Expected {expected_data}, but got {data}"

        print("test_update passed.")

    finally:
        __builtins__.input = original_input


def test_delete():
    # Test data
    data = [{"ID": 1, "Name": "John Doe", "Roll No": "101", "Class": "10-A"}]

    # Simulate user input
    inputs = iter(["1"])

    def mock_input(prompt):
        return next(inputs)

    original_input = __builtins__.input
    __builtins__.input = mock_input

    try:
        # Capture output
        output = io.StringIO()
        with redirect_stdout(output):
            data = delete(data)

        # Expected result
        expected_data = []

        assert data == expected_data, f"Expected {expected_data}, but got {data}"

        print("test_delete passed.")

    finally:
        __builtins__.input = original_input


if __name__ == "__main__":
    test_create()
    test_view()
    test_update()
    test_delete()
