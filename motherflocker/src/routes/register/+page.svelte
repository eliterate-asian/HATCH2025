
<style>
  * {
      box-sizing: border-box;
  }
  .container {
        max-width: 100%;
        margin-left: 10%;
        margin-right: 10%;
        padding: 50px;
        border: 5px solid rgb(78, 75, 78);
        background-color: rgb(78, 75, 78);
        color: rgb(255, 255, 255);
    }

  .dark {
        max-width: 100%;
        background-color: #222;
        color: #eee;
    }
</style>

<div class="dark">
  <div class="container">
  <h1>Register Data</h1>  
<form>
  <label for="aname">Apiary Name:</label><br>
  <input type="text" id="aname" name="aname" value="Hidden Clover Apiary"><br><br>

  <label for="fname">First Name</label><br>
  <input type="text" id="fname" name="fname" value="John"><br><br>

  <label for="lname">Last Name</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>

  <label for="address">Street Address</label><br>
  <input type="text" id="address" name="address" value="100 Main Street"><br><br>
  
  <input type="submit" value="Submit">
</form>
</div></div>

