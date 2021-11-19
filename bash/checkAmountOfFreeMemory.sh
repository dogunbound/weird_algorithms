# gets the available memory in gigabytes. MUST be able to use read command
function bash_get_free_memory_available_gigabytes {
  memInfo="$(free -g | grep "Mem")"
  read -a memInfoArr <<< $memInfo
  freeMemory=${memInfoArr[3]}
  echo $freeMemory
}

freeMem="$(bash_get_free_memory_available_gigabytes)"

echo $freeMem
