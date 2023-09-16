"""EzPyDB - Easy Python DataBase. """

from os.path import exists

from os import mkdir

from pickle import dumps, load, HIGHEST_PROTOCOL

from datetime import datetime

from typing import Any, Union


PYDB_VERSION = 1.0

EXTENSION_DB = 'pydb'
EXTENSION_LOGS = 'pydbl'

SLASH = '\\'

ERROR = -0xe1101

def pydb_log(message: str) -> str:
    """Create PyDB log message."""
    return f'[{datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")}] PyDB: {message}'

def write(path: str, content: Union[str, bytes], append: bool=False, newline: bool=True) -> None:
    """Write file."""
    with open(
        path,

        ('w' if not append else 'a') \
            if isinstance(content, str) else ('wb' if not append else 'ab') \
                if isinstance(content, bytes) else ('w' if not append else 'a')
    ) as file:
        if newline: content += '\n'

        file.write(content)

class PyDB:
    created: bool = False

    directory: str = None

    db_name: str = None

    path: str = None

    lpath: str = None

    logging: bool = True

    db: dict[Any, Any] = {}

    def __init__(self, db_name: str, directory: str=None) -> None:
        """Initialize database."""
        self.db_name = db_name

        self.directory = directory

        self.path = f'{self.directory + (SLASH if not self.directory.endswith(SLASH) else "") if self.directory is not None else ""}{self.db_name}.{EXTENSION_DB}'

        self.lpath = self.path.replace(EXTENSION_DB, EXTENSION_LOGS)

    def use_logs(self, use: bool) -> None:
        """Set logs using."""
        self.logging = use

    def create(self) -> bool:
        """Create database."""
        try:
            if not exists(self.path) and not self.created:
                if self.directory is not None:
                    mkdir(self.directory)

                with open(self.path, 'w') as _: ...

                if self.logging:
                    with open(self.lpath, 'w') as _: ...

                    write(self.lpath, pydb_log(f'Created database {self.db_name}.'), True)

                self.created = True

                return True
            else:
                self.created = True

                return True
        except:
            return False

    def load(self) -> bool:
        """Load database."""
        if not exists(self.path) or self.path is None:
            return False

        with open(self.path, 'rb') as db:
            try:
                self.db = load(db)
            except EOFError:
                print(pydb_log('Tried to read empty database.'))

        self.created = True

        return True

    def create_or_load(self) -> bool:
        """Create or load database."""
        if not exists(self.path) and not self.created:
            return self.create()

        else:
            return self.load()

    def reg_value(self, name: str, value: Any) -> bool:
        """Register value in database."""
        if not self.created:
            return False

        self.db[name] = value

        if self.logging:
            write(self.lpath, pydb_log(f'Registered key "{name}" with initial value "{value}".'), True)

        return True

    def del_value(self, name: str) -> bool:
        """Delete value in database."""
        if not self.created or name not in self.db:
            return False

        self.db.pop(name)

        if self.logging:
            write(self.lpath, pydb_log(f'Deleted key "{name}".'), True)

    def set_value(self, name: str, value: Any) -> bool:
        """Set value in database."""
        if not self.created or name not in self.db:
            return False

        self.db[name] = value

        if self.logging:
            write(self.lpath, pydb_log(f'Updated key "{name}" with value "{value}".'), True)

        return True

    def get_value(self, name: str) -> Union[Any, int]:
        """Get value from database."""
        return self.db[name] if name in self.db else ERROR

    def get_db(self) -> dict[Any, Any]:
        """Get database as dictionary."""
        return self.db

    def commit(self) -> bool:
        """Commit change(s) to database file."""
        if not exists(self.path) or not self.created:
            return False

        write(self.path, dumps(self.db, HIGHEST_PROTOCOL), False, False)

        if self.logging:
            write(self.lpath, pydb_log(f'Commit to database.'), True)

        return True

    def get_version(self) -> float:
        """Get database version."""
        return PYDB_VERSION
