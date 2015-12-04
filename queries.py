__author__ = 'rjain1'

sql1 = """select class_name,count(*) as total_request,
sum(decode(TYPE_OF_ERROR, 0,1,433,1,473,1,474,1,801,1,0)) as success,
sum(decode(TYPE_OF_ERROR, 403,1,408,1,413,1,419,1,439,1,444,1,449,1,450,1,453,1,475,1,476,1,477,1,478,1,479,1,491,1,492,1,493,1,494,1,495,1,496,1,497,1,498,1,507,1,513,1,514,1,601,1,707,1,708,1,709,1,517,1,200,1,201,1,202,1,300,1,303,1,400,1,404,1,600,1,602,1,603,1,0)) as agent_errors,  sum(decode(TYPE_OF_ERROR, 401,1,409,1,410,1,412,1,415,1,416,1,418,1,424,1,425,1,426,1,431,1,432,1,447,1,448,1,1012,1,0)) as site_errors, sum(decode(TYPE_OF_ERROR, 402,1,405,1,406,1,407,1,411,1,414,1,417,1,420,1,421,1,422,1,427,1,428,1,429,1,430,1,434,1,435,1,436,1,437,1,438,1,440,1,441,1,442,1,443,1,445,1,446,1,451,1,452,1,454,1,455,1,456,1,457,1,458,1,459,1,460,1,461,1,462,1,463,1,464,1,465,1,466,1,467,1,468,1,469,1,470,1,471,1,472,1,480,1,481,1,482,1,483,1,484,1,485,1,486,1,510,1,511,1,512,1,515,1,516,1,604,1,605,1,701,1,702,1,703,1,704,1,705,1,706,1,1000,1,1001,1,1002,1,1003,1,1004,1,1005,1,1006,1,1007,1,1008,1,1009,1,1010,1,1011,1,1013,1,505,1,506,1,509,1,518,1,519,1,520,1,521,1,522,1,523,1,524,1,526,1,0)) as uar_errors,
sum(decode(TYPE_OF_ERROR, 200,1,201,1,202,1,300,1,303,1,400,1,404,1,508,1,600,1,602,1,603,1,0)) as infra_errors,
sum(decode(TYPE_OF_ERROR,423,1,0)) as errors_423,
sum(decode(TYPE_OF_ERROR,522,1,0)) as errors_522,
sum(decode(TYPE_OF_ERROR,525,1,0)) as errors_525,
sum(decode(TYPE_OF_ERROR,414,1,0)) as errors_414,
sum(decode(TYPE_OF_ERROR,427,1,0)) as errors_427
from item_errors_24hr it,sum_info si
where si.sum_info_id=it.sum_info_id and it.server_type in
('C','I') and si.is_beta=0 and si.sum_info_id in (select si.sum_info_id from sum_info si,SUM_INFO_SPTD_LOCALE@REPALDA sl
where sl.locale_id in(37) and si.sum_info_id=sl.sum_info_id and si.is_beta=0
and si.is_ready=1 and si.tag_id not in (3,16,8,6,9,62,1,82,86,10,85,25,83,20,24)
and si.class_name in
('NEDBankSADF','SAABSA','ZAAllanGrayInvestments','FNBankZA','SAABSACC','NEDBankCreditsSADF','NEDBankInvestmentDF','ZAInvestecInvestment','StandardSA','ZAOldMutualInvestments','FNBankZARewards','ZAFNBCredits','ZAWoolworthsStoreCard','ZACapitecBank ','ZAPSGOnlineInvestments','NEDBANKSA','ZASanlamGlacier','NEDBANKSALoan','DiscoveryInsuranceSA','NEDBankLoanSADF','ZAFNBInvestments','ZATFGCredits','ZASatrixInvestments','StandardSACC','ZAPicknPayRewards','ZAFNBMortgage','ZAStandardBankOnlineShareTrading','ZAFNBLoan','ZAStandardRewards','ZADinersClubCC','ZANedBankCC','ZAAlexanderForbesInvestments','ZALibertyInvestment','InvestecInvestmentDF','ZAStandardBankUnitTrusts','ZAMomentum','DiscoveryCCSA','ZASAHomeLoans','InvestecBankDF','WesBankZA','ClicksClubCard','ZAEdgarsCC','InvestecLoanDF','ZADisChemRewards','ZAStandardMortgage','InvestecRewardsDF')
and cache_item_id is not null
 and lower(si.class_name) not like ('custom%')
and lower(si.class_name) not like ('dag%')
And Lower(Si.Class_Name) Not In ('bankagent','sitenotsupported')) Group By Class_Name Order By Agent_Errors Desc
"""
