<?php
$firstArg = $argv[1];
$salt = $argv[2];
function cryptstring($what,$SALT){
return crypt($what,$SALT);
}

echo cryptstring($firstArg,$salt);

?>
