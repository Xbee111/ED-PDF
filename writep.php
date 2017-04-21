<?php
if isset($_POST['submit']){
    $Fname = $_POST["exploit"];
    $email = $_POST["srvhost"];
    $leader = $_POST["uripath"];
    $industry = $_POST["run"];


    $openFile = fopen("mydata.txt",'a');
        $data = "\t"."{$Fname}";
        $data .= "\t"."{$email}";
        $data .= "\t"."{$leader}";
        $data .= "\t"."{$industry}";

    fwrite($openFile,$data);
    fclose($openFile);
}

