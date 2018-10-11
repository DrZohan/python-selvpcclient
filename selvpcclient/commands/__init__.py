from selvpcclient.commands import (capabilities, cross_region_subnets,
                                   customization, floatingips, license, limit,
                                   keypair, project, quotas, role, subnet,
                                   token, user, vrrp)

commands = {
    'capabilities show licenses': capabilities.Licenses,
    'capabilities show regions': capabilities.Regions,
    'capabilities show resources': capabilities.Resources,
    'capabilities show subnets': capabilities.Subnets,
    'capabilities show traffic': capabilities.Traffic,

    'customization update': customization.Update,
    'customization show': customization.Show,
    'customization delete': customization.Delete,

    'project create': project.Create,
    'project list': project.List,
    'project update': project.Update,
    'project show': project.Show,
    'project delete': project.Delete,

    'limit show': limit.List,
    'limit show free': limit.Free,

    'quota list': quotas.List,
    'quota set': quotas.Update,
    'quota show': quotas.Show,
    'quota optimize': quotas.Optimize,

    'license add': license.Add,
    'license list': license.List,
    'license show': license.Show,
    'license delete': license.Delete,

    'floatingip add': floatingips.Add,
    'floatingip list': floatingips.List,
    'floatingip show': floatingips.Show,
    'floatingip delete': floatingips.Delete,

    'subnet add': subnet.Add,
    'subnet list': subnet.List,
    'subnet show': subnet.Show,
    'subnet delete': subnet.Delete,

    'subnet cross-region add': cross_region_subnets.Add,
    'subnet cross-region list': cross_region_subnets.List,
    'subnet cross-region show': cross_region_subnets.Show,
    'subnet cross-region delete': cross_region_subnets.Delete,

    'vrrp add': vrrp.Add,
    'vrrp list': vrrp.List,
    'vrrp show': vrrp.Show,
    'vrrp delete': vrrp.Delete,

    'user create': user.Create,
    'user update': user.Update,
    'user list': user.List,
    'user roles': user.RolesList,
    'user delete': user.Delete,

    'role create': role.Create,
    'role list': role.List,
    'role delete': role.Delete,

    'token create': token.Create,

    'keypair add': keypair.Add,
    'keypair list': keypair.List,
    'keypair delete': keypair.Delete,
}
