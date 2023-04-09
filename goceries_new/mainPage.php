<?php
    include('phpTemplates/mainPageHeader.php');
?>


<?php
    //require functions.php file
    include('functions.php');
      include "db_conn.php";
?>

    <!-- CATEGORIES SECTION -->
    <div class="categories">

        <div class="small-container">
            <h2 style="margin-bottom:35px"> <b>Product Categories </b></h2>

            <div class = "row">
                <div class="col-4">
                    <div class="card product_card" style="width: 18rem;">
                        <img src="images/fruit-banana.png" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title main_card_title">Fruits</h5>
                            <p class="card-text">Shop for fresh, juicy and delicious fruits online. Enjoy the natural sweetness of our hand-picked produce delivered to your door.</p>
                            <a href="category-Fruits.php" class="btn btn-primary">Shop more</a>
                        </div>
                    </div>
                </div>

                <div class="col-4">
                    <div class="card product_card" style="width: 18rem;">
                        <img src="images/beverage-applejuice.png" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title main_card_title">Beverages</h5>
                            <p class="card-text">Satisfy your thirst with premium beverages crafted from the finest ingredients. Order now for a refreshing drink experience delivered to you.</p>
                            <a href="category-beverages.php" class="btn btn-primary">Shop more</a>
                        </div>
                    </div>
                </div>

                <div class="col-4">
                    <div class="card product_card" style="width: 18rem;">
                        <img src="images/vegetable-cabbage.png" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title main_card_title">Vegetables</h5>
                            <p class="card-text">Discover flavorful farm-fresh vegetables. Shop online and have quality produce conveniently delivered to your doorstep.</p>
                            <a href="category-vegetables.php" class="btn btn-primary">Shop more</a>
                        </div>
                    </div>
                </div>

                <div class="col-4">
                    <div class="card product_card" style="width: 18rem;">
                        <img src="images/dairy-vitalegg.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title main_card_title">dairy-eggland</h5>
                            <p class="card-text">Indulge in carefully sourced dairy and eggs from top farms and producers. Order online for quality ingredients delivered to your door.</p>
                            <a href="category-dairy & eggs.php" class="btn btn-primary">Shop more</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- TEAM MEMBERS -->
    <?php
        include("team_members.php");
    ?>    

    <?php
        include("phpTemplates/footer.php");
    ?>
