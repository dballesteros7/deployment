from WMCore.Configuration import Configuration

conf = Configuration()
main = conf.section_('main')
srv = main.section_('server')
srv.thread_pool = 5
main.application = 'crabserver'
main.port = 8270
main.index = 'data'

main.authz_defaults = { 'role': None, 'group': None, 'site': None }
main.section_('tools').section_('cms_auth').key_file = "%s/auth/wmcore-auth/header-auth-key" % __file__.rsplit('/', 3)[0]

app = conf.section_('crabserver')
app.admin = 'cms-service-webtools@cern.ch'
app.description = 'CRABServer RESTFull API'
app.title = 'CRABRESTFull'

views = conf.section_('views')

data = views.section_('data')
data.object = 'CRABInterface.RESTBaseAPI.RESTBaseAPI'
data.transformation = 'http://common-analysis-framework.cern.ch/CMSRunAnaly.sh'
data.workflowManager = 'PandaDataWorkflow'
data.phedexurl = 'https://cmsweb.cern.ch/phedex/datasvc/xml/prod/'
data.dbsurl = 'http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet'
data.defaultBlacklist = ['T0_CH_CERN']
data.serverhostcert = "%s/auth/crabserver/dmwm-service-cert.pem" % __file__.rsplit('/', 3)[0]
data.serverhostkey = "%s/auth/crabserver/dmwm-service-key.pem" % __file__.rsplit('/', 3)[0]
data.delegatedn = []
data.credpath = '%s/state/crabserver/proxy/' % __file__.rsplit('/', 4)[0]
data.db = 'CRABServerAuth.dbconfig'
