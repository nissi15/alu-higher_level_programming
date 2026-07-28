# Python - Almost a circle

Object-oriented programming project on inheritance, class and instance
attributes, `*args`, `**kwargs`, JSON serialization and unit testing.

## Files

| File | Description |
| ---- | ----------- |
| `models/base.py` | `Base` class managing the `id` of all other classes and the JSON serialization and deserialization |
| `models/rectangle.py` | `Rectangle` class inheriting from `Base` |
| `models/square.py` | `Square` class inheriting from `Rectangle` |
| `tests/test_models/test_base.py` | Unit tests for `Base` |
| `tests/test_models/test_rectangle.py` | Unit tests for `Rectangle` |
| `tests/test_models/test_square.py` | Unit tests for `Square` |

## Usage

```
python3 -m unittest discover tests
```
