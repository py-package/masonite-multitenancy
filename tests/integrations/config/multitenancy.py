"""multitenancy Settings"""

from masonite.environment import env

#  Loads in the environment variables when this page is imported.

"""
|--------------------------------------------------------------------------
| MultiTenancy
|--------------------------------------------------------------------------
|
| Multitenancy is a feature that allows you to have multiple tenants in your
| application. This is useful for things like a company having multiple
| websites, or a company having multiple apps.
|
"""

TENANTS = {
    "tenant1": {
        "driver": "sqlite",
        "database": env("SQLITE_DB_DATABASE", "tenant1.sqlite3"),
        "prefix": "",
        "log_queries": env("DB_LOG"),
    },
    "tenant2": {
        "driver": "sqlite",
        "database": env("SQLITE_DB_DATABASE", "tenant2.sqlite3"),
        "prefix": "",
        "log_queries": env("DB_LOG"),
    },
}
