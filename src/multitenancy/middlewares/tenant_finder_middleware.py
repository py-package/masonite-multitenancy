from masonite.middleware import Middleware
from ..facades import Tenancy


class TenantFinderMiddleware(Middleware):
    """Middleware to find the tenant for the current request."""

    def before(self, request, response):
        """Find the tenant for the current request."""
        tenant = Tenancy.find_tenant(request)
        if tenant is not None:
            Tenancy.use_tenant(tenant)
            request.tenant = tenant
        return request

    def after(self, request, response):
        """Return the response."""
        return response
