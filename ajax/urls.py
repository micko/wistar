from django.conf.urls import patterns, url

from ajax import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^configJunosInterfaces/$', views.configJunosInterfaces, name='configJunosInterfaces'),
    url(r'^preconfigJunosDomain/$', views.preconfigJunosDomain, name='preconfigJunosDomain'),
    url(r'^preconfigFirefly/$', views.preconfigFirefly, name='preconfigFirefly'),
    url(r'^preconfigLinuxDomain/$', views.preconfigLinuxDomain, name='preconfigLinuxDomain'),
    url(r'^getJunosConfig/$', views.getJunosConfig, name='getJunosConfig'),
    url(r'^getConfigTemplates/$', views.getConfigTemplates, name='getConfigTemplates'),
    url(r'^applyConfigTemplate/$', views.applyConfigTemplate, name='applyConfigTemplate'),
    url(r'^getJunosStartupState/$', views.getJunosStartupState, name='getJunosStartupState'),
    url(r'^getLinuxStartupState/$', views.getLinuxStartupState, name='getLinuxStartupState'),
    url(r'^syncLinkData/$', views.syncLinkData, name='syncLinkData'),
    url(r'^refreshDeploymentStatus/$', views.refreshDeploymentStatus, name='refreshDeploymentStatus'),
    url(r'^refreshHypervisorStatus/$', views.refreshHypervisorStatus, name='refreshHypervisorStatus'),
    url(r'^refreshHostLoad/$', views.refreshHostLoad, name='refreshHostLoad'),
    url(r'^multiCloneTopology/$', views.multiCloneTopology, name='multiCloneTopology'),
    url(r'^deployTopology/$', views.deployTopology, name='deployTopology'),
    url(r'^startTopology/$', views.startTopology, name='startTopology'),
    url(r'^manageDomain/$', views.manageDomain, name='manageDomain'),
    url(r'^manageNetwork/$', views.manageNetwork, name='manageNetwork'),
    url(r'^manageHypervisor/$', views.manage_hypervisor, name='manage_hypervisor'),
    url(r'^executeCli/$', views.executeCli, name='executeCli'),
    url(r'^executeLinuxCli/$', views.executeLinuxCli, name='executeLinuxCli'),
    url(r'^launchWebConsole/$', views.launchWebConsole, name='launchWebConsole'),
    url(r'^pushConfigSet/$', views.pushConfigSet, name='pushConfigSet'),
    url(r'^deleteConfigSet/$', views.deleteConfigSet, name='deleteConfigSet'),
    url(r'^viewNetwork/(?P<network_name>[^/]+)$', views.viewNetwork, name='viewNetwork'),
    url(r'^viewDomain/(?P<domain_id>[^/]+)$', views.viewDomain, name='viewDomain'),
)
