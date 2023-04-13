<?php
session_start();
include "db_conn.php";
?>
<!DOCTYPE html>
<html lang="en">

<head>
  <!-- basic -->
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <!-- mobile metas -->
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="viewport" content="initial-scale=1, maximum-scale=1">
  <!-- site metas -->
  <title>Grocery</title>
  <meta name="keywords" content="">
  <meta name="description" content="">
  <meta name="author" content="">
  <!-- fevicon -->
  <link rel="icon" href="images/fevicon.png" type="image/gif" />
  <!-- bootstrap css -->
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <!-- style css -->
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/main_style.css">
  <!-- Responsive-->
  <link rel="stylesheet" href="css/responsive.css">  
  <!-- Scrollbar Custom CSS -->
  <link rel="stylesheet" href="css/jquery.mCustomScrollbar.min.css">
  <!-- Tweaks for older IEs-->
  <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.css" media="screen">
<!--[if lt IE 9]>
<script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script><![endif]-->
</head>

<body>


<header>
    <!-- header inner -->
    <div class="header-top">
      <div class="header">
        <div class="container-fluid">
          <div class="row">
            <div class="col-xl-2 col-lg-4 col-md-4 col-sm-3 col logo_section">
              <div class="full">
                <div class="center-desk">
                  <div class="logo">
                    <a href = "mainPage.php"><img style="width:200px; height:auto" src="images/logo.png" alt=""></a>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-xl-10 col-lg-8 col-md-8 col-sm-9">
         
               <div class="menu-area">
                <div class="limit-box">
                  <nav class="main-menu ">
                    <ul class="menu-area-main">
                        <?php if (isset($_SESSION['user_id'])&& isset($_SESSION['user_loginname'])){ ?>

                        <li><a href = "mainPage.php">Home</a></li>
                        <li><a href = "category-allProducts.php">Products</a></li>
                        <li><a href = "about.php">About</a></li>
                        <li><a href = "account.php">Hello, <?php echo $_SESSION['user_name']; ?></a></li>
                        <li><a href = "logout.php">Logout</a></li>
                        <li><a href = "cart.php"><i class="fa fa-shopping-cart cart-icon" aria-hidden="true"></i></a></li>
                            <?php } else { ?>

                            <li><a href = "loginregister.php">Sing In</a></li>
                            <li><button class="Join_button"><a href = "register.php">Join</a></button></li>
                            <?php } ?>
                     </ul>
                   </nav>
                 </div>
               </div> 
              </div>
           </div>
         </div>
       </div>
     </div>

    <!-- slider -->
    <section class="slider_section">
      <div id="myCarousel" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
          <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
          <li data-target="#myCarousel" data-slide-to="1"></li>
          <li data-target="#myCarousel" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
          <div class="carousel-item active">

            <div class="container-fluid padding_dd">
              <div class="carousel-caption">
                <div class="row">
                  <div class="col-xl-6 col-lg-6 col-md-6 col-sm-12">
                    <div class="text-bg">
                     <span class="welcome">Welcome To Eco Market</span>
                      <h1 style="margin-bottom:45px">Grocery Shop</h1>
                      <p>From the comfort of your couch, you can now browse through an endless virtual aisle of fresh produce, pantry staples, and gourmet treats, all just a few clicks away on our innovative online grocery shop.</p>
                    </div>
                    <?php if (isset($_SESSION['user_id'])&& isset($_SESSION['user_loginname'])){ ?>
                   
                    <?php } else { ?>
                      <a href = "register.php"><button class="Join_button_slider" style="color:black">Join with us</button></a>
                    <?php } ?>

                  </div>
                  <div class="col-xl-6 col-lg-6 col-md-6 col-sm-12">
                    <div class="images_box">
                      <figure><img style="width:450px; height:auto" src="images/cart.png"></figure>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="carousel-item">

            <div class="container-fluid padding_dd">
              <div class="carousel-caption">

                <div class="row">
                  <div class="col-xl-6 col-lg-6 col-md-6 col-sm-12">
                    <div class="text-bg">
                      <span class="welcome">Welcome To Eco Market</span>
                      <h1>Fresh Fruits & Vegetables</h1>
                      <p>The vibrant hues and crisp textures of fresh fruits and vegetables make for a tantalizing feast for the senses, and their wholesome goodness nourishes both body and soul, providing a bountiful source of vitamins, minerals, and antioxidants to promote vitality and well-being.</p>
                    </div>
                  </div>

                  <div class="col-xl-6 col-lg-6 col-md-6 col-sm-12">
                    <div class="images_box">
                      <figure><img style="width:630px; height:auto" src="images/vegi.png"></figure>
                    </div>
                  </div>
                </div>
              </div>
            </div>

          </div>


          <div class="carousel-item">

            <div class="container-fluid padding_dd">
              <div class="carousel-caption ">
                <div class="row">
                  <div class="col-xl-6 col-lg-6 col-md-6 col-sm-12">
                    <div class="text-bg">
                      <span class="welcome">Welcome To Eco Market</span>
                      <h1>delivered to your doorstep.</h1>
                      <p>With just a few clicks, online doorstep delivery brings the world to your front door, allowing you to indulge in the comforts of home while satisfying your every whim and desire, without ever having to step foot outside.</p>
                    </div>
                  </div>
                  <div class="col-xl-6 col-lg-6 col-md-6 col-sm-12">
                    <div class="images_box">
                      <figure><img style="width:445px; height:auto" src="images/delevery.png"></figure>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <a class="carousel-control-prev" href="#myCarousel" role="button" data-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#myCarousel" role="button" data-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>

</section>
</div>
</header>

