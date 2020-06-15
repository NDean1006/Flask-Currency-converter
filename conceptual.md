### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
	- JS is a scripting language while python is OBJECT-ORIENTED
	>

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you 
  can try to get a missing key (like "c") *without* your programming 
  crashing.
	1. Use .setdefault()
	2. Use .get()
	3. Use the key in dict idiom
	4. Use a try and except block	
	>
- What is a unit test?
	- A unit test is a test method that targets individual blocks of code. 
	>
- What is an integration test?
	- Interrogation testing is a testing method that combines modules of code and tests it a a group
	>
- What is the role of web application framework, like Flask?
	- Flask role is to allow developers a greater degree of efficiency for web http routing 
	>
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
	-query would be used for user provided input and rout should be used for linear progression through routes 
	>
- How do you collect data from a URL placeholder parameter using Flask?
	- "You can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the <variable_name> as a keyword argument. Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>." __Flask quick start__
	>

- How do you collect data from the query string using Flask?
	- request.args
	>
- How do you collect data from the body of the request using Flask?
	- request.data
	>

- What is a cookie and what kinds of things are they commonly used for?
	- a cookie is cached user data. The main purpose of a cookie is to identify users and possibly prepare customized Web pages.
	>

- What is the session object in Flask?
	- A session object is used to track the session data which is a dictionary object that contains a key-value pair of the session variables and their associated values.
	>

- What does Flask's `jsonify()` do?
	-returns a flask.Response() object that already has the appropriate content-type header 'application/json' for use with json responses.
	>
- What was the hardest part of this past week for you?
	- The hardest part of this past week was writing the test cases and getting them to function as intended. methods with flash messages have proven difficult to test. 
	>
- What was the most interesting?
	- back-end development in general is more interesting and enjoyable. 
	
	 
