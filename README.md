<p align="center">
<img src="https://banners.beyondco.de/Masonite%20Multitenancy.png?theme=light&packageManager=pip+install&packageName=masonite-multitenancy&pattern=charlieBrown&style=style_2&description=Multitenancy+package+for+masonite.&md=1&showWatermark=1&fontSize=100px&images=adjustments&widths=50&heights=50">
</p>

<p align="center">
  <a href="https://docs.masoniteproject.com">
    <img alt="Masonite Package" src="https://img.shields.io/static/v1?label=Masonite&message=package&labelColor=grey&color=blue&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAAXNSR0IArs4c6QAAAIRlWElmTU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgEoAAMAAAABAAIAAIdpAAQAAAABAAAAWgAAAAAAAABIAAAAAQAAAEgAAAABAAOgAQADAAAAAQABAACgAgAEAAAAAQAAAA6gAwAEAAAAAQAAAA4AAAAATspU+QAAAAlwSFlzAAALEwAACxMBAJqcGAAAAVlpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KTMInWQAAAnxJREFUKBVNUl1IVEEUPjPObdd1VdxWM0rMIl3bzbVWLSofVm3th0AhMakHHyqRiNSHEAq5b2HSVvoQRUiEECQUQkkPbRslRGigG8auoon2oPSjpev+3PWeZq7eaC5nDt93vplz5txDQJYpNxX4st4JFiwj9aCqmswUFQNS/A2YskrZJPYefkECC2GhQwAqvLYybwXrwBvq8HSNOXRO92+aH7nW8vc/wS2Z9TqneYt2KHjlf9Iv+43wFJMExzO0YE5OKe60N+AOW6OmE+WJTBrg23jjzWxMBauOlfyycsV24F+cH+zAXYUOGl+DaiDxfl245/W9OnVrSY+O2eqPkyz4sVvHoKp9gOihf5KoAVv3hkQgbj/ihG9fI3RixKcUVx7lJVaEc0vnyf2FFll+ny80ZHZiGhIKowWJBCEAKr+FSuNDLt+lxybSF51lo74arqs113dOZqwsptxNs5bwi7Q3q8npSC2AWmvjTncZf1l61e5DEizNn5mtufpsqk5+CZTuq00sP1wkNPv8jeEikVVlJso+GEwRtNs3QeBt2YP2V2ZI3Tx0e+7T89zK5tNASOLEytJAryGtkLc2PcBM5byyUWYkMQpMioYcDcchC6xN220Iv36Ot8pV0454RHLEwmmD7UWfIdX0zq3GjMPG5NKBtv5qiPEPekK2U51j1451BZoc3i+1ohSQ/UzzG5uYFFn2mwVUnO4O3JblXA91T51l3pB3QweDl7sNXMyEjbguSjrPcQNmwDkNc8CbCvDd0+xCC7RFi9wFulD3mJeXqxQevB4prrqgc0TmQ85NG/K43e2UwnMVAJIEBNfWRYR3HfnvivrIzMyo4Hgy+hfscvLo53jItAAAAABJRU5ErkJggg==">
  </a>
  <img alt="GitHub Workflow Status (branch)" src="https://github.com/py-package/masonite-multitenancy/actions/workflows/pythonapp.yml/badge.svg">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/masonite-multitenancy">
  <img src="https://img.shields.io/badge/python-3.6+-blue.svg" alt="Python Version">
  <img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/py-package/masonite-multitenancy?include_prereleases">
  <img alt="License" src="https://img.shields.io/github/license/py-package/masonite-multitenancy">
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

# Masonite Multitenancy (WIP)

Multitenancy package for Masonite!

Multitenancy is a feature that allows you to have multiple tenants in your application. This is useful for things like a company having multiple websites, or a company having multiple apps.

### Features

- [x] Create a new tenant (with domain)
- [x] Tenant specific configurations
- [x] Tenant specific migrations and seeders
- [x] Tenant middleware to specify tenant in request on the fly

### Installation

```bash
pip install masonite-multitenancy
```

### Configuration

Add _`MultitenancyProvider`_ to your project in `config/providers.py`:

```python
# config/providers.py
# ...
from multitenancy import MultitenancyProvider

# ...
PROVIDERS = [
    # ...
    # Third Party Providers
    MultitenancyProvider,
    # ...
]
```

Then you can publish the package resources (if needed) by doing:

```bash
python craft package:publish multitenancy
```

### Usage

You'll get bunch of commands to manage tenants.

**Create a new tenant**

This will prompt few questions just provider answers and that's it.
```bash
python craft tenancy:create
```

> Note: After creating a new tenant, you will need to setup related database configuration in `config/multitenancy.py`.

For example, if your tenant database name is `tenant1`, then you need to add the following to `config/multitenancy.py`:

```python
# config/multitenancy.py

TENANTS = {
  "tenant1": {
    "driver": "sqlite",
    "database": env("SQLITE_DB_DATABASE", "tenant1.sqlite3"),
    "prefix": "",
    "log_queries": env("DB_LOG"),
  },
}
```

You can use any database driver that Masonite supports. For example, if you want to use MySQL, then you can use the following:

```python
# config/multitenancy.py

TENANTS = {
  "tenant1": {
    "driver": "mysql",
    "host": env("DB_HOST"),
    "user": env("DB_USERNAME"),
    "password": env("DB_PASSWORD"),
    "database": env("DB_DATABASE"),
    "port": env("DB_PORT"),
    "prefix": "",
    "grammar": "mysql",
    "options": {
        "charset": "utf8mb4",
    },
    "log_queries": env("DB_LOG"),
  },
}
```

> Note: Make sure you have set the `multitenancy` configuration before running any tenant related commands.

**List all tenants**

```bash
python craft tenancy:list
```

**Delete a tenant**

```bash
# delete a tenant by database name
python craft tenancy:delete --tenants=tenant1
# or
python craft tenancy:delete --tenants=tenant1,tenant2
```

**Delete all tenants**

```bash
python craft tenancy:delete
```

**Migrate a tenant**

```bash
python craft tenancy:migrate --tenants=tenant1
# or
python craft tenancy:migrate --tenants=tenant1,tenant2
```

**Migrate all tenants**
  
```bash
python craft tenancy:migrate
```

Similary you can use `tenancy:migrate:refresh`, `tenancy:migrate:reset`, `tenancy:migrate:status` and `tenancy:migrate:rollback` commands.
All commands will take `--tenants` option to specify tenants if you ever need.

**Seed a tenant**

```bash
python craft tenancy:seed --tenants=tenant1
# or
python craft tenancy:seed --tenants=tenant1,tenant2
```

**Seed all tenants**

```bash
python craft tenancy:seed
```

### Final Step

Now the multitenancy is almost ready to use. The final step is to make use of tenancy middleware. This middleware will be used to specify tenant in request on the fly. So, basically you have to attach this middleware to all the routes that are tenant aware.

```python
# config/routes.py
# ...

Route.get("/", "WelcomeController@show")
Route.get("/tenant-aware-routes", "WelcomeController@show").middleware("multitenancy")
```

In above example, `/tenant-aware-routes` will be tenant aware. It means that if you have tenant setup and you are trying to access `/tenant-aware-routes` then you will get tenant specific items from the database.


### Contributing

Please read the [Contributing Documentation](CONTRIBUTING.md) here.

### Maintainers

- [x] [Yubaraj Shrestha](https://www.github.com/yubarajshrestha)

### License


multitenancy is open-sourced software licensed under the [MIT license](LICENSE).

