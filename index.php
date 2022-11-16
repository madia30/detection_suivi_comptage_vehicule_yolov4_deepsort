<html>

<head>
    
</head>

<body >


    <?php
    #$python = `python python_send_mail.py`; echo $python;
    $command = "python python_send_mail.py";
     $pid = popen( $command,"r");
      while( !feof( $pid ) )
       { 
           echo fread($pid, 256);
            flush(); ob_flush(); 
            usleep(100000); 
        } 
        pclose($pid);

    ?>

</body>
