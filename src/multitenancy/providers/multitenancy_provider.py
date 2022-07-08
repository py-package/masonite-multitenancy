"""A MultitenancyProvider Service Provider."""

from masonite.packages import PackageProvider

from ..middlewares.tenant_finder_middleware import TenantFinderMiddleware
from ..commands.TenancyMigrate import TenancyMigrate
from ..commands.TenancyCreate import TenancyCreate
from ..commands.TenancyList import TenancyList
from ..commands.TenancyDelete import TenancyDelete
from ..commands.TenancyMigrateRefresh import TenancyMigrateRefresh
from ..commands.TenancyMigrateRollback import TenancyMigrateRollback
from ..commands.TenancyMigrateReset import TenancyMigrateReset
from ..commands.TenancyMigrateStatus import TenancyMigrateStatus
from ..commands.TenancySeed import TenancySeed
from ..multitenancy import MultiTenancy


class MultitenancyProvider(PackageProvider):
    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("multitenancy")
            .name("multitenancy")
            .config("config/multitenancy.py", publish=True)
        )

    def register(self):
        super().register()
        self.application.bind("multitenancy", MultiTenancy(self.application))
        self.application.make("middleware").add({"multitenancy": [TenantFinderMiddleware]})
        (
            self.application.make("commands")
            .add(TenancyMigrate(self.application))
            .add(TenancyCreate(self.application))
            .add(TenancyList(self.application))
            .add(TenancyDelete(self.application))
            .add(TenancyMigrateRefresh(self.application))
            .add(TenancyMigrateRollback(self.application))
            .add(TenancyMigrateStatus(self.application))
            .add(TenancyMigrateReset(self.application))
            .add(TenancySeed(self.application))
        )

    def boot(self):
        """Boots services required by the container."""
        pass
