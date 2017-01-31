<!DOCTYPE html>
<html lang="en">
    <head> 
      <meta name="viewport" content="width=device-width, initial-scale=1">

      <!-- Bootstrap CSS -->
      <link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
      
      <!-- Website CSS style -->
      <link rel="stylesheet" type="text/css" href="public/css/main.css">

      <!-- Google Fonts -->
      <link href='https://fonts.googleapis.com/css?family=Passion+One' rel='stylesheet' type='text/css'>
      <link href='https://fonts.googleapis.com/css?family=Oxygen' rel='stylesheet' type='text/css'>

      <!-- CSS modal result -->
      <link rel="stylesheet" type="text/css" href="public/css/modal.css">

      <!-- DateTimePicker CSS -->
      <link rel="stylesheet" href="vendor/datetimepicker/build/css/bootstrap-datetimepicker.min.css" />
      
      <title>PyTV Admin</title>

   </head>   
   <body>



      <div class="container">
         <div class="row main">
            <div>
               <div class="panel-title text-center">
                  <h2 class="title">Emergency Report</h2>
                  <hr/>
               </div>
            </div> 
         
         <div class="main-login main-center">

            <form class="form-horizontal" method="post" action="#">

               <!-- Event -->

               <div class="form-group">
                  <label for="event" class="cols-sm-2 control-label">Event</label>
                  <div class="cols-md-10">
                     <div>
                        <select class="form-control" id="event"  placeholder="Please select the type of Emergency">
                           <option>-select-</option>
                           <option>Huayco</option>
                           <option>Tsunami</option>
                           <option>Epidemia</option>
                           <option>Explosión</option>
                        </select>
                     </div>
                  </div>
               </div>

               <!-- Date -->

               <div class="form-group">
                  <label for="text" class="cols-sm-2 control-label">Date</label>
                  <div class="input-group date col-md-12" id="datepicker">
                     <input class="form-control" type="text" placeholder="dd/mm/aaaa">
                     <span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>
                     </input>
                  </div>
               </div>
               
               <!-- Time -->

               <div class="form-group">
                  <label for="text" class="cols-sm-2 control-label">Time</label>
                  <div class="input-group date col-md-12" id="timepicker">
                     <input class="form-control" type="text" placeholder="hh:mm:ss"></input>
                     <span class="input-group-addon"><span class="glyphicon glyphicon-time"></span></span>
                  </div>
               </div>

               <!-- Latitude -->
               
               <div class="form-group">
                  <label for="text" class="cols-sm-2 control-label">Latitude</label>
                  <div class="cols-md-10">
                     <input class="form-control" type="text"></input>
                  </div>
               </div>

               <!-- Longitude -->
               
               <div class="form-group">
                  <label for="text" class="cols-sm-2 control-label">Longitude</label>
                  <div class="cols-md-10">
                     <input class="form-control" type="text"></input>
                  </div>
               </div>

               <!-- Reference -->
               
               <div class="form-group">
                  <label for="text" class="cols-sm-2 control-label">Reference</label>
                  <div class="cols-md-10">
                     <input class="form-control" type="text"></input>
                  </div>
               </div>




               <!-- Submit -->

               <div class="form-group" data-toggle="modal" data-target="#login-modal">
                  <button type="button" class="btn btn-primary btn-lg btn-block login-button">Submit</button>
               </div>



               <!-- Modal Result -->
 
               <div class="modal fade" id="login-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">
                  <div class="modal-dialog">
                     <div class="loginmodal-container">
                        <h1>Are you sure?</h1><br>
                        <form>
                           <input type="text" name="user" placeholder="Result 1">
                           <input type="text" name="pass" placeholder="Result 2">
                           <input type="submit" name="login" class="login loginmodal-submit" value="Send Alert!">
                        </form>
                        <div class="login-help">
                           <a href="#">Cancel</a>
                        </div>               
                     </div>
                  </div>
               </div>


               </form>
            </div>
         </div>
      </div>






      <script type="text/javascript" src="vendor/jquery/jquery-3.1.1.min.js"></script>
      <script type="text/javascript" src="vendor/moment/moment.js"></script>
      <script type="text/javascript" src="vendor/bootstrap/js/transition.js"></script>
      <script type="text/javascript" src="vendor/bootstrap/js/collapse.js"></script>
      <script type="text/javascript" src="vendor/bootstrap/js/bootstrap.min.js"></script>
      <script type="text/javascript" src="vendor/datetimepicker/build/js/bootstrap-datetimepicker.min.js"></script>
      <script type="text/javascript">
         $(function () {
            $('#datepicker').datetimepicker({
               format: 'DD/MM/YYYY',
               showTodayButton: true,
               showClose: true,
               showClear: true,
            });
         });
      </script>
      <script type="text/javascript">
         $(function () {
            $('#timepicker').datetimepicker({
               format: 'LTS',
               showTodayButton: true,
               showClose: true,
               showClear: true,
            });
         });
      </script>


   </body>
</html>