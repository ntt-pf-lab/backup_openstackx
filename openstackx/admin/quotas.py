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

    def update(self, tenant_id, metadata_items=None,
               injected_file_content_bytes=None, volumes=None, gigabytes=None,
               ram=None, floating_ips=None, instances=None, injected_files=None,
               cores=None):

        body = {'quota': {
            'tenant_id': tenant_id,
            'metadata_items': metadata_items,
            'injected_file_content_bytes': injected_file_content_bytes,
            'volumes': volumes,
            'gigabytes': gigabytes,
            'ram': ram,
            'floating_ips': floating_ips,
            'instances': instances,
            'injected_files': injected_files,
            'cores': cores,
        }}

        for key in body['quota'].keys():
            if body['quota'][key] == None:
                body['quota'].pop(key)

        return self._update('/admin/quotas/%s' % (tenant_id), body)

    def delete(self, tenant_id):
        self._delete("/admin/quotas/%s" % (tenant_id))

