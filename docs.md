<h2 align="center"><i>class <b>PyDB</b></i></h2>
<p align="center"><b>Initalization (__init__/constructor):</b></p>

<p align="center"><b><code>Initialization(db_name: string, directory: str=None) -> None</code></b></p>
<p align="center"><b>Takes first argument (<code>db_name</code>) as database name. Should be string, can be any string.</b></p>
<p align="center"><b>Takes second optional argument (<code>directory</code>) in which directory database will be placed.</b></p><br>

<p align="center"><b>Basically initialises database, forms database paths, etc. Returns nothing.</b></p>

<hr>

<p align="center"><b><code>use_logs(use: bool) -> None</code></b></p>
<p align="center"><b>Takes the first argument (<code>use</code>) as the logging state. Should be True/False.</b></p><br>

<p align="center"><b>Sets logging to True or False. Returns nothing.</b></p>

<hr>

<p align="center"><b><code>create() -> bool</code></b></p>
<p align="center"><b>Takes no arguments.</b></p><br>

<p align="center"><b>Creates database file (and logging file if logging is used). Returns result of database creation (True - success, False - failure).</b></p>

<hr>

<p align="center"><b><code>load() -> bool</code></b></p>
<p align="center"><b>Takes no arguments.</b></p><br>

<p align="center"><b>Loads the database. If database is empty, may return "Tried to read empty database. Returns the result of loading the database (True - success, False - failure).</b></p>

<hr>

<p align="center"><b><code>create_or_load() -> bool</code></b></p>
<p align="center"><b>Takes no arguments.</b></p><br>

<p align="center"><b>Creates database if none exists. Loads the database if it exists. Returns result of creating/loading database.</b></p>

<hr>

<p align="center"><b><code>reg_value(name: str, value: Any) -> bool</code></b></p>
<p align="center"><b>Takes first argument (<code>name</code>) as value key.</b></p>
<p align="center"><b>Takes second argument (<code>value</code>) as value.</b></p><br>

<p align="center"><b>Registers value in database. Applies only after <code>commit()</code>. Returns the result of registering value.</b></p>

<hr>

<p align="center"><b><code>set_value(name: str, value: Any) -> bool</code></b></p>
<p align="center"><b>Takes first argument (<code>name</code>) as value key.</b></p>
<p align="center"><b>Takes second argument (<code>value</code>) as value.</b></p><br>

<p align="center"><b>Updates value in database. Updates only if value already exists in database. Applies only after <code>commit()</code>. Returns the result of updating value.</b></p>

<hr>

<p align="center"><b><code>del_value(name: str) -> bool</code></b></p>
<p align="center"><b>Takes first argument (<code>name</code>) as value key.</b></p><br>

<p align="center"><b>Deletes value in database. Deletes value only if it exists in database. Applies only after <code>commit()</code>. Returns the result of deleting value.</b></p>

<hr>

<p align="center"><b><code>get_value( name: str) -> Union[Any, int]</code></b></p>
<p align="center"><b>Takes first argument (<code>name</code>) as value key.</b></p>

<p align="center"><b>Get value from database. Returns value only if value exists, else returns ERROR/-0xe1101[-921857]. Returns the value.</b></p>

<hr>

<p align="center"><b><code>get_db() -> dict[Any, Any]</code></b></p>
<p align="center"><b>Takes no arguments.</b></p>

<p align="center"><b>Returns database as dictionary.</b></p>

<hr>

<p align="center"><b><code>commit() -> bool</code></b></p>
<p align="center"><b>Takes no arguments.</b></p>

<p align="center"><b>Commits all changes to database. Returns the result of commit.</b></p>

<hr>

<p align="center"><b><code>get_version() -> float</code></b></p>
<p align="center"><b>Takes no arguments.</b></p>

<p align="center"><b>Returns database version.</b></p>

<hr>

<h2 align="center"><i><b>Example.</b></i></h2>

<i>Example so you can use PyDB right now.</i>

<i><b>
```python
from ezpydb import PyDB, ERROR # PyDB.


db = PyDB('my_database', 'db_directory') # Initialize database with name 'my_database', and place it in directory 'db_directory' (optional).

if not db.create_or_load(): # Create database if none exists, or load database.
    print('Failed to create database.') # Handle error.

while True:
    uinput = input('PyDB Command: ')

    command = uinput.split(' ')[0]

    if command == 'Register': # Register command.
        data = uinput.split(' ')[1:]

        if not db.reg_value(data[0], data[1]): # Register value with name data[0] and value data[1].
            print('Failed to register value.') # Handle error.

    elif command == 'Set': # Update value.
        data = uinput.split(' ')[1:]

        if not db.set_value(data[0], data[1]): # Update value with name data[0] and value data[1]
            print('Failed to update value.') # Handle error.

    elif command == 'Get': # Get value.
        key = uinput.split(' ')[1]

        out = db.get_value(key)

        print('Failed to get value.' if out == ERROR else out) # Print value or print error.

    elif command == 'Delete': # Delete value.
        key = uinput.split(' ')[1]

        if not db.del_value(key): # Delete key.
            print('Failed to delete value.') # Handle error.

    elif command == 'Commit': # Commit all changes.
        if not db.commit(): # Commit.
            print('Failed to commit.') # Handle errors.

    elif command == 'DB': # Print database as dict.
        print(db.get_db()) # Print.

    elif command == 'Version': # Print database version.
        print(db.get_version()) # Print.
```
</i></b>

<hr>

<p align="center"><i><b>PyDB v1.0 BETA.</b></i></p>
