1]
intent=Communicate_people
entities="{"contact":{"start":8,"end":13,"body":"shoot","suggested":true,"value":"shoot"}}"
contact=shoot

2]
intent=get_search
entities=Object {}

3]
intent=get_search
entities="{"search_query":{"start":11,"end":17,"body":"google","suggested":true,"value":"google"}}"

intent=get_search
search_query=google

4]

===
google search response
ERR:

{"error_message": "invalid literal for int() with base 10: 'Home Page of Geoffrey Hinton'", "traceback": "Traceback (most recent call last):\n\n  File \"/opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv18_2/local/lib/python2.7/site-packages/tastypie/resources.py\", line 202, in wrapper\n    response = callback(request, *args, **kwargs)\n\n  File \"/opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv18_2/local/lib/python2.7/site-packages/tastypie/resources.py\", line 433, in dispatch_list\n    return self.dispatch('list', request, **kwargs)\n\n  File \"/opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv18_2/local/lib/python2.7/site-packages/tastypie/resources.py\", line 465, in dispatch\n    response = method(request, **kwargs)\n\n  File \"/opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv18_2/local/lib/python2.7/site-packages/tastypie/resources.py\", line 1298, in get_list\n    bundles.append(self.full_dehydrate(bundle, for_list=True))\n\n  File \"/opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv18_2/local/lib/python2.7/site-packages/tastypie/resources.py\", line 853, in full_dehydrate\n    bundle.data[field_name] = field_object.dehydrate(bundle, for_list=for_list)\n\n  File \"/opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv18_2/local/lib/python2.7/site-packages/tastypie/fields.py\", line 139, in dehydrate\n    return self.convert(current_object)\n\n  File \"/opt/lampp/htdocs/ash3_opt_www/www2/python/venv/venv18_2/local/lib/python2.7/site-packages/tastypie/fields.py\", line 238, in convert\n    return int(value)\n\nValueError: invalid literal for int() with base 10: 'Home Page of Geoffrey Hinton'\n"}


goog succes data
callQueryApi onSuccess res

'{"meta":{"limit":20,"next":null,"offset":0,"previous":null,"total_count":10},
"objects":[
	{
		"displayLink":"www.cs.toronto.edu",
		"formattedUrl":"www.cs.toronto.edu/~hinton/",
		"htmlSnippet":"I now work part-time for <b>Google</b> as a Distinguished Researcher and part-time for <br>\nthe University of Toronto as a Distinguished Emeritus Professor. For much of the<br>\n&nbsp;...",
		"htmlTitle":"Home Page of Geoffrey Hinton",
		"link":"http://www.cs.toronto.edu/~hinton/",
		"resource_uri":"/api/v1/get_search/None/",
		"title":"Home Page of Geoffrey Hinton"
	},
	{
		"displayLink":"merlot.usc.edu",
		"formattedUrl":"merlot.usc.edu/cs402-f13/googlegroup.html",
		"htmlSnippet":"Aug 21, 2013 <b>...</b> If you use gmail from <b>Google</b> Apps at USC, then option (1) is not available to you. <br>\nYour only option is to use a separate gmail account for our&nbsp;...",
		"htmlTitle":"<b>Google</b> Group - CSCI 402, Fall 2013, Both Sections",
		"link":"http://merlot.usc.edu/cs402-f13/googlegroup.html",
		"resource_uri":"/api/v1/get_search/None/",
		"title":"Google Group - CSCI 402, Fall 2013, Both Sections"
	},
		{"displayLink":"www.cs.rutgers.edu","formattedUrl":"www.cs.rutgers.edu/~mlittman/courses/cs105-07a/googletest1.html","htmlSnippet":"This is a word (sort of) that I concocted on January 3, 2006 and verified that it was <br>\nunknown to <b>Google</b>. (Did you mean: &quot;<b>google</b> discovery&quot;). This page has a&nbsp;...","htmlTitle":"<b>Google</b> Test: Linked Page","link":"http://www.cs.rutgers.edu/~mlittman/courses/cs105-07a/googletest1.html","resource_uri":"/api/v1/get_search/None/","title":"Google Test: Linked Page"},{"displayLink":"www.cs.rutgers.edu","formattedUrl":"https://www.cs.rutgers.edu/resources/show/.../googleauthenticator","htmlSnippet":"Aug 27, 2015 <b>...</b> <b>Google</b> Authenticator is a system of Time Based One Time Password from <br>\nRFC6238. It is often used as part of a Two Factor Authentication for&nbsp;...","htmlTitle":"Enabling <b>Google</b> Authenticator on CS Linux Machine","link":"https://www.cs.rutgers.edu/resources/show/howto/googleauthenticator","resource_uri":"/api/v1/get_search/None/","title":"Enabling Google Authenticator on CS Linux Machine"},{"displayLink":"www.cs.rutgers.edu","formattedUrl":"https://www.cs.rutgers.edu/.../prof-santosh-nagarakatte-awarded-google-grant /","htmlSnippet":"Feb 15, 2014 <b>...</b> Santosh Nagarakatte, who has just received a <b>Google</b> Faculty Research Award. <br>\nHe was awarded an amount of $63500 for his project entitled&nbsp;...","htmlTitle":"Santosh Nagarakatte awarded <b>Google</b> grant","link":"https://www.cs.rutgers.edu/news/articles/2014/02/15/prof-santosh-nagarakatte-awarded-google-grant/","resource_uri":"/api/v1/get_search/None/","title":"Santosh Nagarakatte awarded Google grant"},{"displayLink":"www1.cs.columbia.edu","formattedUrl":"www1.cs.columbia.edu/~mkamvar/publications/CHI_06.pdf","htmlSnippet":"A Large Scale Study of Wireless Search Behavior: <b>Google</b> Mobile Search. <br>\nMaryam Kamvar. 1,2. , Shumeet Baluja. 1,3. {maryam, shumeet} @ <b>google</b>.com. 1<br>\n.","htmlTitle":"A Large Scale Study of Wireless Search Behavior: <b>Google</b> Mobile <b>...</b>","link":"http://www1.cs.columbia.edu/~mkamvar/publications/CHI_06.pdf","resource_uri":"/api/v1/get_search/None/","title":"A Large Scale Study of Wireless Search Behavior: Google Mobile ..."},{"displayLink":"merlot.usc.edu","formattedUrl":"merlot.usc.edu/cs530-s10/googlegroup.html","htmlSnippet":"Sep 17, 2012 <b>...</b> We will use a <b>Google</b> Group for class related communications. The <b>Google</b> Group <br>\nis basically used as a mailing list. This is not the same list as&nbsp;...","htmlTitle":"<b>Google</b> Group - CSCI 530, Spring 2010","link":"http://merlot.usc.edu/cs530-s10/googlegroup.html","resource_uri":"/api/v1/get_search/None/","title":"Google Group - CSCI 530, Spring 2010"},{"displayLink":"www.cs.utexas.edu","formattedUrl":"www.cs.utexas.edu/users/ear/cs349/GoogleQueryResearch.html","htmlSnippet":"<b>Google</b> Query Completion as Social Science Research. 1. Do the following <br>\nexperiment at least three times: a. Choose your favorite search engine. Write <br>\ndown&nbsp;...","htmlTitle":"<b>Google</b> Query Completion as Social Science Research","link":"http://www.cs.utexas.edu/users/ear/cs349/GoogleQueryResearch.html","resource_uri":"/api/v1/get_search/None/","title":"Google Query Completion as Social Science Research"},{"displayLink":"www.cs.man.ac.uk","formattedUrl":"www.cs.man.ac.uk/~david/schools/Google.pdf","htmlSnippet":"How does <b>Google</b> decide which results you may be interested in? <b>Google</b> is not <br>\nthe first Search Engine, earlier were, for example,. Altavista and Yahoo. <b>Google</b>&nbsp;...","htmlTitle":"How does <b>Google</b> work?","link":"http://www.cs.man.ac.uk/~david/schools/Google.pdf","resource_uri":"/api/v1/get_search/None/","title":"How does Google work?"},{"displayLink":"www.cs.rutgers.edu","formattedUrl":"www.cs.rutgers.edu/~mlittman/courses/cs105-07b/googletest1.html","htmlSnippet":"How Does <b>Google</b> Find Pages? This page has little purpose other than to include <br>\nthe word &quot;googleseekeasy&quot;. This is a word (sort of) that I concocted on&nbsp;...","htmlTitle":"<b>Google</b> Test: Linked Page","link":"http://www.cs.rutgers.edu/~mlittman/courses/cs105-07b/googletest1.html","resource_uri":"/api/v1/get_search/None/","title":"Google Test: Linked Page"}]}'

