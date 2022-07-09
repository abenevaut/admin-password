<?php
$handle	= opendir(".");
$projectContents = '';
$projectsListIgnore = array('.','..');
while ($file = readdir($handle)) {
  if (is_dir($file) && !in_array($file, $projectsListIgnore)) {
    $projectContents .= '<li><a href="'.$file.'">'.$file.'</a></li>';
  }
}
closedir($handle);
echo $projectContents ? $projectContents : ''; ?>