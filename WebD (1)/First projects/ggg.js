function delete(file_name)
{
    var r = confirm("Are you sure you want to delete this Image?")
    if(r == true)
    {
        $.ajax({
          url: 'delete.php',
          data: {'file' : "<?php echo dirname(__FILE__) . '/uploads/'?>" + file_name },
          success: function (response) {
             // do something
          },
          error: function () {
             // do something
          }
        });
    }
}