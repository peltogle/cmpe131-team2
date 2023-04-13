<?php
session_start();
include('db_conn.php');

if (isset($_SESSION['user_id']) && isset($_SESSION['user_loginname'])) {
 ?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Products | Go!Ceries</title>

    <!-- Add boostrap CSS-->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <!-- sweet alert -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/sweetalert/2.1.2/sweetalert.min.js" integrity="sha512-AA1Bzp5Q0K1KanKKmvN/4d3IRKVlv9PYgwFPvm32nPO6QS8yH1HO7LbgB1pgiOxPtfeg5zEn2ba64MUcqJx6CA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <!-- OWN CSS -->
    <link rel="stylesheet" href="css/style.css">
    <style>
      .account-info{
        margin-top:160px;
      }
      .td_topic{
        font-size:18px;
        font-weight:700;
        padding-bottom:10px;
        width:450px;
      }
      .btnSubmit{
        width: 120px;
        height: 40px;
        border-radius: 10px;
        background: black;
        color:#00ff22;
        transition:500ms;
        font-weight:500;
      }
      .btnSubmit:hover{
        background: #00ff22;
        color:black;
      }
    </style>
</head>

<body>
    <!-- HEADER -->
    <?php
        include('phpTemplates/header.php');
    ?>

    <div class="account-info">
        <div class="container account-container">
            <div>
              <h2 style="text-align:center"><b> Account Information</b></h2>

                <table style="width:80%">
                  <tr>
                  <td class="td_topic">User Information</td>
                  </tr>
                  <tr>
                    <td>Name:</td>
                    <td><?php echo $_SESSION['user_name']; ?></td>
                  </tr>
                  <tr>
                    <td>User Name:</td>
                    <td><?php echo $_SESSION['user_loginname']; ?></td>
                  </tr>
                </table>
                <hr>
                <table style="width:80%">
                  <tr>
                    <td class="td_topic">Contact Information</td>
                  </tr>
                  <tr>
                    <td>Email Address:</td>
                    <td><?php echo $_SESSION['user_email']; ?></td>
                  </tr>
                  <tr>
                    <td>Shipping Address:</td>
                    <td>
                    <?php
                    $result0 = mysqli_query($conn, "SELECT * FROM users INNER JOIN payments ON users.user_id = payments.payment_user_id WHERE users.user_id='" . $_SESSION["user_id"] . "'");
                    if ($row = mysqli_fetch_array($result0)){
                      echo $row["payment_address"];
                      echo ", ";
                      echo $row["payment_city"];
                      echo ", ";
                      echo $row["payment_state"];
                      echo " ";
                      echo $row["payment_zip"];

                  }else {
                    echo"No shipping address to show";
                  }
                  ?>
                  </td>
                  </tr>
                </table>
                <hr>
              <table style="width:80%">
                <tr>
                  <td class="td_topic">Change password</td>
                </tr>
                <form name="frmChange" method="post" action="" onSubmit="return validatePassword()">
                  <div style="width:500px;">
                    <div class="message"><?php if(isset($message)) { echo $message; } ?></div>
                      <table border="0" cellpadding="10" cellspacing="0" width="500" align="center" class="tblSaveForm">
                        <tr>
                          <td width="40%"><label>Current Password</label></td>
                          <td width="60%"><input type="password" name="currentPassword" class="txtField"/><span id="currentPassword"  class="required"></span></td>
                        </tr>
                        <tr>
                          <td><label>New Password</label></td>
                          <td><input type="password" name="newPassword" class="txtField"/><span id="newPassword" class="required"></span></td>
                        </tr>
                        <td><label>Confirm Password</label></td>
                        <td><input type="password" name="confirmPassword" class="txtField"/><span id="confirmPassword" class="required"></span></td>
                        </tr>
                        <tr>
                          <td colspan="2"><button class="change_password_btn"><input type="submit" name="submit" value="Submit" class="btnSubmit"></button></td>
                        </tr>
                      </table>
                  </div>
                </form>
              </table>
              <hr>
              <table style="width:80%">
              <tr>
                <td class="td_topic">Order history</td>
              </tr>
              <tr>
                <?php
                  $orderid = mysqli_query($conn, "SELECT users.user_id, orders.user_ID, orders.order_ID FROM users INNER JOIN orders ON users.user_id = orders.user_ID WHERE users.user_id='" . $_SESSION["user_id"] . "'");

                  if(mysqli_num_rows($orderid) > 0){ // to check any rows exists or not
                    echo '<td> Your order number(s) is/are: </td> ';
                    while($row = mysqli_fetch_array($orderid)) {
                      echo '<tr><td>'.$row["order_ID"].',</td></tr>';
                    }
                  }else {
                    echo "You don't have any order yet";
                  }
                  ?>
                </tr>
              </table>
            </div>
          </div>
        </div>

        <script>
        function validatePassword() {
          var currentPassword,newPassword,confirmPassword,output = true;

          currentPassword = document.frmChange.currentPassword;
          newPassword = document.frmChange.newPassword;
          confirmPassword = document.frmChange.confirmPassword;

          if(!currentPassword.value) {
            currentPassword.focus();
            document.getElementById("currentPassword").innerHTML = "This field is required";
            output = false;
          }
          else if(!newPassword.value) {
            newPassword.focus();
            document.getElementById("newPassword").innerHTML = "This field is required";
            output = false;
          }
          else if(!confirmPassword.value) {
            confirmPassword.focus();
            document.getElementById("confirmPassword").innerHTML = "This field is required";
            output = false;
          }
          if(newPassword.value != confirmPassword.value) {
            newPassword.value="";
            confirmPassword.value="";
            newPassword.focus();
            document.getElementById("confirmPassword").innerHTML = "New password and confirmation password do not match";
            output = false;
          }
          return output;
        }
      </script>

<?php
    include('phpTemplates/footer.php');
    if (count($_POST) > 0) {
    $result = mysqli_query($conn, "SELECT * FROM users WHERE user_id='" . $_SESSION["user_id"] . "'");

  $pass = md5($_POST["currentPassword"]);
  $hashNewPass = md5($_POST["newPassword"]);
    $row = mysqli_fetch_array($result);
    if ($_POST["currentPassword"] === $row["user_password"] || $pass === $row["user_password"] ) {
        mysqli_query($conn, "UPDATE users set user_password='" . $hashNewPass . "' WHERE user_id='" . $_SESSION["user_id"] . "'");
        echo '<script>swal("Password Updated!", "Your password has been successfully updated.", "success");</script>';
    } else
        echo '<script>swal("Oops", "Current password is not correct", "error")</script>';
}
?>
<?php
}else{
     header("Location: loginregister.php?error=You need to login before shopping");
     exit();
}
 ?>
