# Just used to slice and dice this json into different forms
import json


def folder_mapping():
    foldermapping = '''[
                   {
                   "inFolder" : false,
                   "xmlName" : "InstalledPackage",
                   "suffix" : "installedPackage",
                   "directoryName" : "installedPackages",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "suffix" : "labels",
                   "metaFile" : false,
                   "childXmlNames" : [
                      "CustomLabel"
                   ],
                   "xmlName" : "CustomLabels",
                   "directoryName" : "labels"
                },
                {
                   "inFolder" : false,
                   "xmlName" : "StaticResource",
                   "suffix" : "resource",
                   "directoryName" : "staticresources",
                   "metaFile" : true
                },
                {
                   "inFolder" : false,
                   "xmlName" : "Scontrol",
                   "suffix" : "scf",
                   "directoryName" : "scontrols",
                   "metaFile" : true
                },
                {
                   "inFolder" : false,
                   "xmlName" : "ApexComponent",
                   "suffix" : "component",
                   "directoryName" : "components",
                   "metaFile" : true
                },
                {
                   "inFolder" : false,
                   "xmlName" : "ApexPage",
                   "suffix" : "page",
                   "directoryName" : "pages",
                   "metaFile" : true
                },
                {
                   "inFolder" : false,
                   "xmlName" : "Queue",
                   "suffix" : "queue",
                   "directoryName" : "queues",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "ExternalDataSource",
                   "suffix" : "dataSource",
                   "directoryName" : "dataSources",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "Role",
                   "suffix" : "role",
                   "directoryName" : "roles",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "Group",
                   "suffix" : "group",
                   "directoryName" : "groups",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "suffix" : "object",
                   "metaFile" : false,
                   "childXmlNames" : [
                      "CustomField",
                      "BusinessProcess",
                      "CompactLayout",
                      "RecordType",
                      "WebLink",
                      "ValidationRule",
                      "NamedFilter",
                      "SharingReason",
                      "ListView",
                      "FieldSet"
                   ],
                   "xmlName" : "CustomObject",
                   "directoryName" : "objects"
                },
                {
                   "inFolder" : false,
                   "xmlName" : "ReportType",
                   "suffix" : "reportType",
                   "directoryName" : "reportTypes",
                   "metaFile" : false
                },
                {
                   "inFolder" : true,
                   "xmlName" : "Report",
                   "suffix" : "report",
                   "directoryName" : "reports",
                   "metaFile" : false
                },
                {
                   "inFolder" : true,
                   "xmlName" : "Dashboard",
                   "suffix" : "dashboard",
                   "directoryName" : "dashboards",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "AnalyticSnapshot",
                   "suffix" : "snapshot",
                   "directoryName" : "analyticSnapshots",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "Layout",
                   "suffix" : "layout",
                   "directoryName" : "layouts",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "CustomPageWebLink",
                   "suffix" : "weblink",
                   "directoryName" : "weblinks",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "QuickAction",
                   "suffix" : "quickAction",
                   "directoryName" : "quickActions",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "FlexiPage",
                   "suffix" : "flexipage",
                   "directoryName" : "flexipages",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "CustomTab",
                   "suffix" : "tab",
                   "directoryName" : "tabs",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "CustomApplicationComponent",
                   "suffix" : "customApplicationComponent",
                   "directoryName" : "customApplicationComponents",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "CustomApplication",
                   "suffix" : "app",
                   "directoryName" : "applications",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "Letterhead",
                   "suffix" : "letter",
                   "directoryName" : "letterhead",
                   "metaFile" : false
                },
                {
                   "inFolder" : true,
                   "xmlName" : "EmailTemplate",
                   "suffix" : "email",
                   "directoryName" : "email",
                   "metaFile" : true
                },
                {
                   "inFolder" : false,
                   "xmlName" : "Flow",
                   "suffix" : "flow",
                   "directoryName" : "flows",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "suffix" : "workflow",
                   "metaFile" : false,
                   "childXmlNames" : [
                      "WorkflowFieldUpdate",
                      "WorkflowKnowledgePublish",
                      "WorkflowTask",
                      "WorkflowAlert",
                      "WorkflowSend",
                      "WorkflowOutboundMessage",
                      "WorkflowRule"
                   ],
                   "xmlName" : "Workflow",
                   "directoryName" : "workflows"
                },
                {
                   "inFolder" : false,
                   "suffix" : "assignmentRules",
                   "metaFile" : false,
                   "childXmlNames" : [
                      "AssignmentRule"
                   ],
                   "xmlName" : "AssignmentRules",
                   "directoryName" : "assignmentRules"
                },
                {
                   "inFolder" : false,
                   "suffix" : "autoResponseRules",
                   "metaFile" : false,
                   "childXmlNames" : [
                      "AutoResponseRule"
                   ],
                   "xmlName" : "AutoResponseRules",
                   "directoryName" : "autoResponseRules"
                },
                {
                   "inFolder" : false,
                   "suffix" : "escalationRules",
                   "metaFile" : false,
                   "childXmlNames" : [
                      "EscalationRule"
                   ],
                   "xmlName" : "EscalationRules",
                   "directoryName" : "escalationRules"
                },
                {
                   "inFolder" : false,
                   "xmlName" : "PostTemplate",
                   "suffix" : "postTemplate",
                   "directoryName" : "postTemplates",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "ApprovalProcess",
                   "suffix" : "approvalProcess",
                   "directoryName" : "approvalProcesses",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "HomePageComponent",
                   "suffix" : "homePageComponent",
                   "directoryName" : "homePageComponents",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "HomePageLayout",
                   "suffix" : "homePageLayout",
                   "directoryName" : "homePageLayouts",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "CustomObjectTranslation",
                   "suffix" : "objectTranslation",
                   "directoryName" : "objectTranslations",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "ApexClass",
                   "suffix" : "cls",
                   "directoryName" : "classes",
                   "metaFile" : true
                },
                {
                   "inFolder" : false,
                   "xmlName" : "ApexTrigger",
                   "suffix" : "trigger",
                   "directoryName" : "triggers",
                   "metaFile" : true
                },
                {
                   "inFolder" : false,
                   "xmlName" : "Profile",
                   "suffix" : "profile",
                   "directoryName" : "profiles",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "PermissionSet",
                   "suffix" : "permissionset",
                   "directoryName" : "permissionsets",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "DataCategoryGroup",
                   "suffix" : "datacategorygroup",
                   "directoryName" : "datacategorygroups",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "RemoteSiteSetting",
                   "suffix" : "remoteSite",
                   "directoryName" : "remoteSiteSettings",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "AuthProvider",
                   "suffix" : "authprovider",
                   "directoryName" : "authproviders",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "CustomSite",
                   "suffix" : "site",
                   "directoryName" : "sites",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "suffix" : "sharingRules",
                   "metaFile" : false,
                   "childXmlNames" : [
                      "LeadOwnerSharingRule",
                      "LeadCriteriaBasedSharingRule"
                   ],
                   "xmlName" : "LeadSharingRules",
                   "directoryName" : "leadSharingRules"
                },
                {
                   "inFolder" : false,
                   "suffix" : "sharingRules",
                   "metaFile" : false,
                   "childXmlNames" : [
                      "CampaignOwnerSharingRule",
                      "CampaignCriteriaBasedSharingRule"
                   ],
                   "xmlName" : "CampaignSharingRules",
                   "directoryName" : "campaignSharingRules"
                },
                {
                   "inFolder" : false,
                   "suffix" : "sharingRules",
                   "metaFile" : false,
                   "childXmlNames" : [
                      "CaseOwnerSharingRule",
                      "CaseCriteriaBasedSharingRule"
                   ],
                   "xmlName" : "CaseSharingRules",
                   "directoryName" : "caseSharingRules"
                },
                {
                   "inFolder" : false,
                   "suffix" : "sharingRules",
                   "metaFile" : false,
                   "childXmlNames" : [
                      "ContactOwnerSharingRule",
                      "ContactCriteriaBasedSharingRule"
                   ],
                   "xmlName" : "ContactSharingRules",
                   "directoryName" : "contactSharingRules"
                },
                {
                   "inFolder" : false,
                   "suffix" : "sharingRules",
                   "metaFile" : false,
                   "childXmlNames" : [
                      "OpportunityOwnerSharingRule",
                      "OpportunityCriteriaBasedSharingRule"
                   ],
                   "xmlName" : "OpportunitySharingRules",
                   "directoryName" : "opportunitySharingRules"
                },
                {
                   "inFolder" : false,
                   "suffix" : "sharingRules",
                   "metaFile" : false,
                   "childXmlNames" : [
                      "AccountOwnerSharingRule",
                      "AccountCriteriaBasedSharingRule"
                   ],
                   "xmlName" : "AccountSharingRules",
                   "directoryName" : "accountSharingRules"
                },
                {
                   "inFolder" : false,
                   "suffix" : "sharingRules",
                   "metaFile" : false,
                   "childXmlNames" : [
                      "CustomObjectOwnerSharingRule",
                      "CustomObjectCriteriaBasedSharingRule"
                   ],
                   "xmlName" : "CustomObjectSharingRules",
                   "directoryName" : "customObjectSharingRules"
                },
                {
                   "inFolder" : false,
                   "suffix" : "sharingRules",
                   "metaFile" : false,
                   "childXmlNames" : [
                      "UserMembershipSharingRule",
                      "UserCriteriaBasedSharingRule"
                   ],
                   "xmlName" : "UserSharingRules",
                   "directoryName" : "userSharingRules"
                },
                {
                   "inFolder" : false,
                   "xmlName" : "Community",
                   "suffix" : "community",
                   "directoryName" : "communities",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "CallCenter",
                   "suffix" : "callCenter",
                   "directoryName" : "callCenters",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "EntitlementProcess",
                   "suffix" : "entitlementProcess",
                   "directoryName" : "entitlementProcesses",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "MilestoneType",
                   "suffix" : "milestoneType",
                   "directoryName" : "milestoneTypes",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "EntitlementTemplate",
                   "suffix" : "entitlementTemplate",
                   "directoryName" : "entitlementTemplates",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "ConnectedApp",
                   "suffix" : "connectedApp",
                   "directoryName" : "connectedApps",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "Network",
                   "suffix" : "network",
                   "directoryName" : "networks",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "SamlSsoConfig",
                   "suffix" : "samlssoconfig",
                   "directoryName" : "samlssoconfigs",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "SynonymDictionary",
                   "suffix" : "synonymDictionary",
                   "directoryName" : "synonymDictionaries",
                   "metaFile" : false
                },
                {
                   "inFolder" : false,
                   "xmlName" : "Settings",
                   "suffix" : "settings",
                   "directoryName" : "settings",
                   "metaFile" : false
                }
                ]'''
    return json.loads(foldermapping)


for x in folder_mapping():
    #print('"{}"'.format(x['directoryName']) + "  :  " + "[{" + '"{}"  :  "{}"'.format("xmlName", x['xmlName']) + " , " + '"{}"  :  "{}"'.format("suffix", x['suffix']) + "}]" + ",")

    #Suffixes
    #print('"{}"'.format(x['suffix']) + ',')

    #directory mapping
    #print('"{}" : "{}",'.format(x['directoryName'], x['xmlName']))

    #directories
    #print('"{}",'.format(x['directoryName']))