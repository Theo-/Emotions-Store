<html>
<head>
<title>Registration</title>
<style> 

#form 
{
height: 500px;
width: 70%;
margin: 0 auto;
border: 2px;
border-color: blue;
border-radius: 25px;
border-style: solid;
}

form 
{
position:absolute;
padding: 50px 50px 50px 50px;
}

input
{
margin-bottom: 50px;
}
</style>
<link rel="stylesheet" type="text/css" href="custom.css"/>
</head>
	<body> 
<div id="menu">
	<ul>
		<li><a href="index.html">Emotions Store</a></li>
		<li><a href="catalogue.py">Catalogue</a></li>
		<li><a href="login.html">Login</a></li>
		<li><a href="Registration.php">Register</a></li>
	</ul>
</div>

<br/>
	<div id="form">
	<form name="New User" action="Register.pl" method="post">
	<h2>Register</h2>
	
	First and last name: <input type="text" name="Name"></br>
	UserName:            <input type="text" name="UserName"> </br>
	Password:            <input type="password" name="password"> </br>
	Confirm Password:    <input type="password" name="ConfPassword"> </br>
	<input type="submit">	
	</div>
</form>
 
	</body>
</html>
