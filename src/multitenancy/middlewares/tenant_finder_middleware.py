from masonite.middleware import Middleware
from ..models.Tenant import Tenant

class TenantFinderMiddleware(Middleware):
    """Middleware to find the tenant for the current request."""

    def before(self, request, response):
        """Find the tenant for the current request."""
        tenant = Tenant.where("domain", request.get_host()).first()
        if tenant:
            request.tenant = tenant
        return request

    def after(self, request, response):
        """Return the response."""
        return response