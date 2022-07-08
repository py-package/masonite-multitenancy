from masonite.middleware import Middleware
from ..models.Tenant import Tenant


class TenantFinderMiddleware(Middleware):
    """Middleware to find the tenant for the current request."""

    def before(self, request, response):
        from wsgi import application

        """Find the tenant for the current request."""
        tenant = (
            Tenant.where("domain", request.get_host())
            .or_where("database", request.get_subdomain())
            .first()
        )
        if tenant:
            request.tenant = tenant
            tenancy = application.make("multitenancy")
            tenancy.setup_connection(tenant)

        return request

    def after(self, request, response):
        """Return the response."""
        return response
