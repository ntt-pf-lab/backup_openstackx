from openstackx.api import base


class TenantQuotaSet(base.Resource):
    def __repr__(self):
        return "<TenantQuotaSet: %s>" % self.id

    def delete(self):
        self.manager.delete(self)

    def update(self, *args, **kwargs):
        self.manager.update(self.tenant_id, *args, **kwargs)


class TenantQuotaSetManager(base.ManagerWithFind):
    resource_class = TenantQuotaSet

    def list(self):
        return self._list("/admin/quotas", "quota_set_list")

    def get(self, tenant_id):
        return self._get("/admin/quotas/%s" % (tenant_id), "quota_set")

    def update(self, tenant_id, **kwargs):
        """ Update TenantQuotaSet

            Accepted Keyword arguments:
                metadata_items -- integer
                injected_file_content_bytes -- integer
                volumes -- integer
                gigabytes -- integer
                ram -- integer (in bytes)
                floating_ips -- integer
                instances -- integer
                injected_files -- integer
                cores -- integer
        """
        body = {'quota': kwargs}

        return self._update('/admin/quotas/%s' % (tenant_id), body)

    def delete(self, tenant_id):
        self._delete("/admin/quotas/%s" % (tenant_id))

