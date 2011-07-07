from openstackx.api import base


class Quota(base.Resource):
    def __repr__(self):
        return "<Quota>"

    def delete(self):
        self.manager.delete(self)

    def update(self, *args, **kwargs):
        self.manager.update(self.project_id, *args, **kwargs)


class QuotaManager(base.ManagerWithFind):
    resource_class = Quota

    def list(self):
        return self._list("/admin/quotas", "quotas")

    def get(self, project_id):
        return self._get("/admin/quotas/%s" % (project_id), "quota")

    def create(self, project_id, resource, limit):
        body = {"quota": {'project_id': project_id, 'resource': resource,
                          'hard_limit': limit}}

        return self._create('/admin/quotas', body, "quota")

    def update(self, project_id, **kwargs):
        attributes = {}
        for arg in kwargs:
            attributes[arg] = kwargs[arg]

        body = {"quota": attributes}

        return self._update('/admin/quotas/%s' % (project_id), body)

    def delete(self, project_id):
        self._delete("/admin/quotas/%s" % (project_id))

