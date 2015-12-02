__author__ = 'rjain1'

sql1 = """Select class_name,total_request,success,agent_errors,site_errors,uar_errors,Infra_error from (select si.class_name,
sum(num_errors) as total_request,
sum(decode(sss.TYPE_OF_ERROR, 0,num_errors,433,num_errors,473,num_errors,474,num_errors,801,num_errors,0)) as success,
sum(decode(sss.TYPE_OF_ERROR, 403,num_errors,408,num_errors,413,num_errors,419,num_errors,439,num_errors,444,num_errors,449,num_errors,450,num_errors,453,num_errors,475,num_errors,476,num_errors,477,num_errors,478,num_errors,479,num_errors,491,num_errors,492,num_errors,493,num_errors,494,num_errors,495,num_errors,496,num_errors,497,num_errors,498,num_errors,507,num_errors,513,num_errors,514,num_errors,601,num_errors,707,num_errors,708,num_errors,709,num_errors,517,num_errors,0)) as agent_errors,
sum(decode(sss.TYPE_OF_ERROR, 401,num_errors,409,num_errors,410,num_errors,412,num_errors,415,num_errors,416,num_errors,418,num_errors,424,num_errors,425,num_errors,426,num_errors,431,num_errors,432,num_errors,447,num_errors,448,num_errors,1012,num_errors,0)) as site_errors,
sum(decode(sss.TYPE_OF_ERROR, 402,num_errors,406,num_errors,407,num_errors,411,num_errors,414,num_errors,417,num_errors,420,num_errors,421,num_errors,422,num_errors,423,num_errors,427,num_errors,428,num_errors,429,num_errors,430,num_errors,434,num_errors,435,num_errors,436,num_errors,437,num_errors,438,num_errors,440,num_errors,441,num_errors,442,num_errors,443,num_errors,445,num_errors,446,num_errors,451,num_errors,452,num_errors,454,num_errors,455,num_errors,456,num_errors,457,num_errors,458,num_errors,459,num_errors,460,num_errors,461,num_errors,462,num_errors,463,num_errors,464,num_errors,465,num_errors,466,num_errors,467,num_errors,468,num_errors,469,num_errors,470,num_errors,471,num_errors,472,num_errors,480,num_errors,481,num_errors,482,num_errors,483,num_errors,484,num_errors,485,num_errors,486,num_errors,510,num_errors,511,num_errors,512,num_errors,515,num_errors,516,num_errors,604,num_errors,605,num_errors,701,num_errors,702,num_errors,703,num_errors,704,num_errors,705,num_errors,706,num_errors,1000,num_errors,1001,num_errors,1002,num_errors,1003,num_errors,1004,num_errors,1005,num_errors,1006,num_errors,1007,num_errors,1008,num_errors,1009,num_errors,1010,num_errors,1011,num_errors,1013,num_errors,505,num_errors,506,num_errors,509,num_errors,518,num_errors,519,num_errors,520,num_errors,521,num_errors,522,num_errors,523,num_errors,524,num_errors,526,num_errors,0)) as uar_errors,
sum(decode(sss.TYPE_OF_ERROR, 200,num_errors,201,num_errors,202,num_errors,300,num_errors,303,num_errors,400,num_errors,404,num_errors,508,num_errors,600,num_errors,602,num_errors,603,num_errors,0)) as Infra_error

from site_stats_suminfo sss, sum_info si
where si.sum_info_id=sss.sum_info_id
and si.class_name in
 ('RBCDirectInvestments','RoyalBank','SunlifePlanMembersCA','RBCBranchInvestments','RoyalBankCC','TDBankCA','Desjardins','CATDBankInvestments','BMOInvestorLine','TDBankCACredits','CACapitalOnceCostcoCC','CIBCBank','RBCLoan','CAScotiaCC','BancorpSouthCC','VancityCA','RBCSecurities','CAScotiabank','BMOMosaikCard','RBCMortgage','CATireFinancialCC','CanadaAmexCreditCard','VancityCACC','ChaseCAOnlineCreditCard','CAINGDirect','mbanx','CIBCCC')

--'MBNACredits','CapitalOneCreditsDF',
and timestamp >(sysdate-1)
and server_type in ('C','I')
group by si.class_name)
order by agent_errors desc
"""