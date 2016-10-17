# import json
# import urllib2
# def get_gender():
# 	myKey = "rntTzGQuvyeeMSkJZL"
# 	get_name="https://gender-api.com/get?key=" + str(myKey) + "&name= "+ "Ricky"
# 	data = json.load(urllib2.urlopen(get_name))
# 	print "Gender: " + data["gender"]; #Gender: male
# get_gender()	

# MY_API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# from scopus.scopus_api import ScopusAbstract

# ab = ScopusAbstract("Property and Political Order in Africa")
# print(ab.bibtex)
# print(ab.ris)
import scholarly

# print(next(scholarly.search_author('Steven A. Cholewiak')))
title_list=['Strength in NumbersThe Political Power of Weak Interests ', 'Industrial Constructions The Sources of German Industrial Power ', 'Governing Ideas Strategies for Innovation in France and Germany ', 'Reforming Capitalism Institutional Change in the German Political Economy ', 'Holding the Shop Together German Industrial Relations in the PostWar Era ', 'The Second Industrial Divide Possibilities for Prosperity ', 'Remaking the Italian Economy ', 'Regional Advantage Culture and Competition in Silicon Valley and Route', 'Governance of the American Economy ', 'Governing Capitalist Economies Performance and Control of Economic Sectors ', 'Capitalists Against Markets The Making of Labor Markets and Welfare States ', 'in the United States and Sweden ', 'How Institutions Evolve The Political Economy of Skills in Germany, Britain, the United States, and Japan ', 'What Unions No Longer Do ', 'Varieties of Liberalization and the New Politics of Social Solidarity ', 'Political Power and Corporate Control The New Global Politics of Corporate Governance ', 'Smoke & Mirrors, Inc Accounting for Capitalism ', 'Entrepreneurial States Reforming Corporate Governance in France, Japan, ', 'and Korea ', 'Public Law and Private Power Corporate Governance Reform in the Age of Finance Capitalism ', 'Quiet Politics and Business Power Corporate Control in Europe and Japan ', 'Capitalizing on Crisis The Political Origins of the Rise of Finance ', 'The Regulation SchoolA Critical Introduction', 'Manufacturing Possibilities Creative Action and Industrial Recomposition in the United States, Germany, and Japan ', 'Markets on Trial The Economic Sociology of the US. Financial Crisis ', 'Coping With Crisis Government Reactions to the Great Recession ','MITI and the Japanese Miracle ', 'Information, Incentives, and Bargaining in the Japanese Economy ', 'Unmaking the Japanese Miracle ', 'Japan Network Economy ', 'Changing Japanese Capitalism Societal Coordination and Institutional Adjustment ', 'Welfare and Capitalism in Postwar Japan ', 'Spending Without Taxation FILP and the Politics of Public Finance in Japan ', 'Welfare Through Work Conservative Ideas, Partisan Dynamics, and Social Protection in Japan ', 'Hedge Fund Activism in Japan The Limits of Shareholder Primacy ', 'Governing the Market Economic Theory and the Role of Government in East Asian Industrialization ', 'The Developmental State ', 'StateDirected Development Political Power and Industrialization in the Global Periphery ', 'Innovation and the State Political Choice and Strategies for Growth in Israel, ', 'Taiwan, and Ireland ', 'Development, Democracy, and Welfare States Latin America, East ', 'Asia, and Eastern Europe ', 'Dependent Development The Alliance of Multinationals, State, and Local Capital in Brazil ', 'Political Competition, Partisanship, and Policy Making in Latin ', 'American Public Utilities ', 'Colonialism and Postcolonial Development Spanish America in Comparative Perspective ', 'ModelsofEconomicLiberalizationBusiness,Workers,', 'and Compensation in Latin America, Spain and Portugal ', 'Hierarchical Capitalism in Latin America Business, Labor, and the Challenges of Equitable Development ', 'Foreign and Domestic Investment Argentina The Politics of Privatized Infrastructure ', 'Private Wealth and Public Revenue in Latin America Business Power and Tax Politics ']



print len(title_list)
def send_2_txt(l):
	f= open('output.txt','a')
	for i in title_list:
		x= scholarly.search_pubs_query(i)
		print >>f, next(x)
		# else:
			# print None

send_2_txt(title_list)