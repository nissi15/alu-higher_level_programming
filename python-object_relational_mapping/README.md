# Python - Object-relational mapping

Scripts connecting Python to a MySQL database, first with the `MySQLdb`
module using raw SQL queries, then with the `SQLAlchemy` ORM using mapped
model classes.

## Files

| File | Description |
| ---- | ----------- |
| `0-select_states.py` | Lists all states from `hbtn_0e_0_usa` |
| `1-filter_states.py` | Lists states whose name starts with `N` |
| `2-my_filter_states.py` | Lists states matching a name given as argument |
| `3-my_safe_filter_states.py` | Same as above, safe from SQL injection |
| `4-cities_by_state.py` | Lists all cities with their state from `hbtn_0e_4_usa` |
| `5-filter_cities.py` | Lists all cities of a state given as argument |
| `model_state.py` | `State` class mapped to the table `states` |
| `6-model_state.py` | Creates the `states` table |
| `7-model_state_fetch_all.py` | Lists all `State` objects |
| `8-model_state_fetch_first.py` | Prints the first `State` object |
| `9-model_state_filter_a.py` | Lists `State` objects containing the letter `a` |
| `10-model_state_my_get.py` | Prints the `State` matching a name given as argument |
| `11-model_state_insert.py` | Adds the `State` "Louisiana" |
| `12-model_state_update_id_2.py` | Renames the `State` with `id = 2` to "New Mexico" |
| `13-model_state_delete_a.py` | Deletes `State` objects containing the letter `a` |
| `model_city.py` | `City` class mapped to the table `cities` |
| `14-model_city_fetch_by_state.py` | Prints all `City` objects with their state |

## Usage

```
./0-select_states.py <mysql username> <mysql password> <database name>
```
