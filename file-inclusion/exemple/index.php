<?php

echo "<html><head><title>Fail include</title></head><body>";
echo "<h3>Fail include</h3>";
echo "<h4>It's seem possible to hack this site!</h4>";
echo "<div id='content'>";

/**
*
* Ici on voit tres que la variable $_GET
* n'est pas proteger. Elle ne subit aucun traitement,
* elle pourrait contenir n'importe qu'elle valeur.
*
*/

if (isset($_GET['page']) && !empty($_GET['page'])) {
   include $_GET['page'];
}
else {
  echo '<fieldset>';
  include 'home.php';
  echo '</fieldset><br/>';
}

echo "</div><div id='foot'>Antoine Benevaut</div></body></html>";

?>