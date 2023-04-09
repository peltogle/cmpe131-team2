<style>
    @import url('https://fonts.googleapis.com/css2?family=Alkatra:wght@600&family=Edu+NSW+ACT+Foundation:wght@500;600&display=swap');

    body{
        display:flex;
        align-items:center;
        justify-content:center;
    }
    .order_on_the_way{
        height:50vh;
    }
    .main_div{
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    h2{
        font-family: 'Alkatra', cursive;
        font-weight:600;
        font-size:40px;
    }
    h3{
        font-family: 'Edu NSW ACT Foundation', cursive;
        font-size:20px;
        font-weight:600;
    }
    .logo{
        width:125px;
        height:auto;
    }
    .back_home{
        border:none;
        background-color:#ffffff;
        box-shadow: rgba(0, 0, 0, 0.25) 0 8px 15px;
        border-radius:10px;
        cursor:pointer;
        transition:500ms;
    }
    .back_home:hover{
        box-shadow: rgb(15 255 78 / 60%) 0 8px 15px;
    }
</style>
<body>
    <div class="main_div">
        <div>
            <h2>your order is on the way</h2>
        </div>
        <div>
            <img class="order_on_the_way" src="images/order_on_the_way.png" alt="">
        </div>
        <div>
            <h3>Thanks for choosing us!</h3>
        </div>
        <div>
            <a href="mainPage.php"><button class="back_home"><img class="logo" src="images/logo.png" alt=""></button></a>
        </div>
    </div>
    
</body>
