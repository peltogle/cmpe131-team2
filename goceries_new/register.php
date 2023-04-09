
<html>

<head>
<title>Login and Register</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw==" crossorigin="anonymous" referrerpolicy="no-referrer" />

<style>
      @import url('https://fonts.googleapis.com/css?family=Raleway:400,700');

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;	
        font-family: Raleway, sans-serif;
    }

    body {
        background: #000000;		
    }

    .container {
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
    }

    .screen {		
        background: linear-gradient(90deg, #000000, #3b7219);		
        position: relative;	
        height: 600px;
        width: 400px;	
        box-shadow: 0px 0px 24px #5C5696;
    }

    .screen__content {
        z-index: 1;
        position: relative;	
        height: 100%;
    }

    .screen__background {		
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: 0;
        -webkit-clip-path: inset(0 0 0 0);
        clip-path: inset(0 0 0 0);	
    }

    .screen__background__shape {
        transform: rotate(45deg);
        position: absolute;
    }

    .screen__background__shape1 {
        height: 520px;
        width: 520px;
        background: #FFF;	
        top: -50px;
        right: 120px;	
        border-radius: 0 72px 20px 0;
    }

    .screen__background__shape2 {
        height: 220px;
        width: 220px;
        background: #3f9c39;	
        top: -172px;
        right: 0;	
        border-radius: 32px;
    }

    .screen__background__shape3 {
        height: 540px;
        width: 190px;
        background: linear-gradient(113deg, #000000, #17ff00);
        top: -24px;
        right: 0;	
        border-radius: 32px;
    }

    .screen__background__shape4 {
        height: 400px;
        width: 200px;
        background: #7CFC00;	
        top: 420px;
        right: 50px;	
        border-radius: 60px;
    }

    .login {
        width: 320px;
        padding: 30px;
        padding-top: 15px;
    }

    .login__field {
        padding: 20px 0px;	
        position: relative;	
    }

    .login__icon {
        position: absolute;
        top: 30px;
        color: #7875B5;
    }

    .login__input {
        border: none;
        border-bottom: 2px solid #D1D1D4;
        background: none;
        padding: 10px;
        padding-left: 24px;
        font-weight: 700;
        width: 75%;
        transition: .2s;
    }

    .login__input:active,
    .login__input:focus,
    .login__input:hover {
        outline: none;
        border-bottom-color: #6A679E;
    }

    .login__submit {
        background: #fff;
        font-size: 14px;
        margin-top: 30px;
        padding: 16px 20px;
        border-radius: 26px;
        border: 1px solid #D4D3E8;
        text-transform: uppercase;
        font-weight: 700;
        display: flex;
        align-items: center;
        width: 100%;
        color: #4C489D;
        box-shadow: 0px 2px 2px #5C5696;
        cursor: pointer;
        transition: .2s;
    }

    .login__submit:active,
    .login__submit:focus,
    .login__submit:hover {
        border-color: #6A679E;
        outline: none;
    }

    .button__icon {
        font-size: 24px;
        margin-left: auto;
        color: #7875B5;
    }

    .social-login {	
        position: absolute;
        height: 140px;
        width: 160px;
        text-align: center;
        bottom: 0px;
        right: 0px;
        color: #fff;
    }

    .social-icons {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .social-login__icon {
        padding: 20px 10px;
        color: #fff;
        text-decoration: none;	
        text-shadow: 0px 0px 8px #7875B5;
    }

    .social-login__icon:hover {
        transform: scale(1.5);	
    }
    .Join_button{
        display: flex;
        align-items: center;
        appearance: none;
        background-color: #000000;
        border: 2px solid #1A1A1A;
        border-radius: 15px;
        box-sizing: border-box;
        color: #FFFFFF;
        cursor: pointer;
        display: inline-block;
        font-family: Roobert,-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";
        font-size: 16px;
        font-weight: 600;
        line-height: normal;
        margin: 0;
        min-height: 40px;
        min-width: 0;
        outline: none;
        padding: 5px 24px;
        text-align: center;
        text-decoration: none;
        transition: all 300ms cubic-bezier(.23, 1, 0.32, 1);
        user-select: none;
        -webkit-user-select: none;
        touch-action: manipulation;
        width: 100%;
        will-change: transform;
    }
    .Join_button:disabled {
        pointer-events: none;
    }

    .Join_button:hover {
        box-shadow: 0px 2px 2px #78ff67;
        transform: translateY(-2px);
        color: #00ff22 !important;
    }

    .Join_button:active {
        box-shadow: none;
        transform: translateY(0);
    }

    .Join_button > a{
        color: #FFFFFF !important;
    }

    .Join_button > a:hover{
        color: #00ff22 !important;
    }
</style>
</head>
<body>
<div class ="background">
  <div class ="form-box">
  <div class = "login-box">

  <div class="container">
	<div class="screen">
		<div class="screen__content">
      <!-- <img src="images/logo.png" alt=""> -->
          <form id="login" action = "registercheck.php" method="POST" class= "input login">
            <?php if (isset($_GET['error'])) { ?>
                    <p class="error"><?php echo $_GET['error']; ?></p>
                  <?php } ?>

                  <?php if (isset($_GET['success'])) { ?>
                       <p class="success"><?php echo $_GET['success']; ?></p>
                  <?php } ?>

                    <?php if (isset($_GET['userid'])) { ?>
                        <div class="login__field">
                            <input type="text"
                                    name="userid"
                                    class="input-field login__input"
                                    placeholder="Username"
                                    value="<?php echo $_GET['userid']; ?>">
                        </div>
                    <?php }else{ ?>
                        <div class="login__field">
                            <input type="text"
                                    name="userid"
                                    class="input-field login__input"
                                    placeholder="Username">
                        </div>
                    <?php }?>

                    <?php if (isset($_GET['username'])) { ?>
                        <div class="login__field">
                                        <input type="text"
                                            name="username"
                                            class="input-field login__input"
                                            placeholder="Full Name"
                                            value="<?php echo $_GET['username']; ?>">
                        </div>
                    <?php }else{ ?>
                        <div class="login__field">
                                <input type="text"
                                    name="username"
                                    class="input-field login__input"
                                    placeholder="Full Name">
                        </div>
                    <?php }?>

                    <div class="login__field">                                    
                        <input type ="email"  name="email" id="email" class="input-field login__input" placeholder="Email Address" >
                    </div>
                    <div class="login__field">
                        <input type ="text" name="password" id="password" class="input-field login__input" placeholder="Enter Your Password" >
                    </div>
                    <div class="login__field">
                        <input type ="text" name="re_password" id="re_password" class="input-field login__input" placeholder="Re-Enter Your Password" >
                    </div>
                    <div class="login__field">
                        <input type="checkbox" required class="check-box"<span style="margin-right:10px; font-weight: bold !important;">I agree to the terms of serivice</span>
                    </div>
                    <button type="submit" class="submit-button Join_button">Register</button>
                    </form>
		            </div>
		<div class="screen__background">
			<span class="screen__background__shape screen__background__shape4"></span>
			<span class="screen__background__shape screen__background__shape3"></span>		
			<span class="screen__background__shape screen__background__shape2"></span>
			<span class="screen__background__shape screen__background__shape1"></span>
		</div>		
	</div>
</div>

    </div>

<script>
  var x = document.getElementById("login");
  var y = document.getElementById("register");
  var z = document.getElementById("bt");
  function login(){
    x.style.left="-400px"
    y.style.left= "50px";
    z.style.left= "110px";
  }function register(){
    x.style.left="50px"
    y.style.left= "450px";
    z.style.left= "0px";
  }
  </script>

</body>
</html>
