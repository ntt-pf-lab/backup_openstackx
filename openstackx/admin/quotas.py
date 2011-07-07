from openstackx.api import base


class Quota(base.Resource):
    def __repr__(self):
        return "<Quota>"

    def delete(self):
        self.manager.delete(self)

    def update(self, *args, **kwargs):
        self.manager.update(self.tenant_id, *args, **kwargs)


class QuotaManager(base.ManagerWithFind):
    resource_class = Quota

    def list(self):
        return self._list("/admin/quotas", "quotas")

    def get(self, tenant_id):
        return self._get("/admin/quotas/%s" % (tenant_id), "quota")

    def update(self, tenant_id, **kwargs):
        attributes = {}
        for arg in kwargs:
            attributes[arg] = kwargs[arg]

        body = {"quota": attributes}

        return self._update('/admin/quotas/%s' % (tenant_id), body)

    def delete(self, tenant_id):
        self._delete("/admin/quotas/%s" % (tenant_id))

