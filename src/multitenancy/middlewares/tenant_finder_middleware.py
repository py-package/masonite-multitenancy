from masonite.middleware import Middleware


class TenantFinderMiddleware(Middleware):
    """Middleware to find the tenant for the current request."""

    def before(self, request, response):
        return request.app.make("multitenancy").find_tenant(request)

    def after(self, request, response):
        """Return the response."""
        return response
