# Evil-Twin
### Simple implementation in Python for the evil twin attack

<h3>About the attak:</h3>
<p>
  An <b>evil twin</b> is a fraudulent Wi-Fi access point that appears to be legitimate but is set up to eavesdrop on wireless communications.<br>
  The evil twin is the wireless LAN equivalent of the phishing scam.<br><br>
  This type of attack may be used to steal the passwords of unsuspecting users, either by monitoring their connections or by phishing, which involves
   setting up a fraudulent web site and luring people there.  
</p>

<h3>Method</h3>
<p>
  The attacker snoops on Internet traffic using a bogus wireless access point. <br>
  Unwitting web users may be invited to log into the attacker's server, prompting them to enter sensitive information such as usernames and
  passwords.<br><br>
  Fake access points are set up by configuring a wireless card to act as an access point. 
  They are hard to trace since they can be shut off instantly.<br><br>
  In this project: <br>
  The attack is split into two parts.<br>
  In the first part the attacker defines an access point and a user that he will want to attack,and then he disconnects the user from the network
  <br>
  In the second part the attacker establishes a fake access point with the same name of the network he is attacking, and lets the disconnected user
  connect to it.
  </p>
  
  <h3>Requierement</h3>
  <p>
  <ul>
    <li>
      Linux operating system, with two network interfaces,so that both can enter monitor mode.
      </li>
    <li>
      Python 2.7 and above
    </li>
  </ul>
  </p>
  
  <h4>How to run the attack</h4>
  <p>
  You can run the attack from the Python file:  EvilTwin.py.<br>
  All you need to do is just to run the code on the terminal ► <b> sudo python EvilTwin.py </b>
  <br>
  There you will be asked to enter the names of the interfaces you would like to use.<br>
  The first is for sniffing net after attack nets.<br>
  The second to create the fake access point.<br>
  It is also possible to run only the second part of the attack, and only create a fake access point.
  <br>
  All you need is to run this on the terminal ► <b> sudo python runFakeAP.py </b>
  <br>
  If you just want to disconnect a user from the network, you can do so by setting line 93 in the 'EvilTwin.py' script as a comment.
  </p>
  
  
  
  
  
