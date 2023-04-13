
<?php
session_start();

if (isset($_SESSION['user_id']) && isset($_SESSION['user_loginname'])) {

 ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Products | Go!Ceries</title>

    <!-- Add boostrap CSS-->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <!-- OWN CSS -->
    <link rel="stylesheet" href="css/style.css">




</head>


<body>

    <!-- HEADER -->
    <?php
        include('phpTemplates/header.php');
    ?>

    <!-- include functions controller -->
    <?php
        include('functions.php');
    ?>

    <!-- ALL PRODUCTS SECTION -->
    <div class="categories all-products">

        <div class="small-container">
            <h2><b>All Products</b></h2>

        <form class="sort_by">
          <label for ="sort"></label>
          <select name="list" id="list" accesskey="target">
            <option value='none' selected>Choose a category</option>
            <option value="category-allproducts.php">All Products</option>
            <option value="category-fruits.php">Fruits</option>
            <option value="category-vegetables.php">Vegetables</option>
            <option value="category-dairy & eggs.php">Dairy & Eggs</option>
            <option value="category-beverages.php">Beverage</option>
          </select>
          <input class="go_btn" type=button value="Go" onclick="goToNewPage()" />
        </form>

            <div class = "row">
            <?php foreach ($productsArray as $product){ ?>
                <div class="card all_product_crad" style="width: 18rem;">
                    <img src="images/<?php echo $product['product_imagename']?>" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title"><p class="card_titile"><?php echo $product['product_name'] ?></p></h5>
                        <p class="card-text sub_title"><?php echo 'Weight ~ ' . $product['product_weight'] . 'lb' ?></p>
                        <p class="card-text amount"><?php echo '$'. $product['product_price'] ?></p>
                        <a href="<?php printf('%s?product_id=%s','productDetails.php', $product['product_id'])?>" class="btn btn-primary">Add to cart</a>
                    </div>
                </div>
            <?php }?>

            </div>

            <!-- <div class = "products-button">
                <span title='Fruits'><a href="category-fruits.php">1</a></span>
                <span title='Vegetables'><a href="category-vegetables.php">2</a></span>
                <span title='Dairy & Eggs'><a href="category-dairy & eggs.php">3</a></span>
                <span title='Beverages'><a href="category-beverages.php">4</a></span>
            </div> -->
            <hr>
        </div>

    </div>

<!-- FOOTER -->
<?php
    include('phpTemplates/footer.php');
?>
<?php
}else{
     header("Location: loginregister.php?error=You need to login before shopping");
     exit();
}
 ?>
