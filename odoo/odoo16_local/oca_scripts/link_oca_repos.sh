cd /opt/odoo/oca_repos
for dir in *
  do
  if [ $dir = "server" ]
    then
    continue
  else
    for subdir in $dir/*
      do
      if [ -d $subdir ]
        then
        echo "Enlazando $subdir"
        ln -s /opt/odoo/oca_repos/$subdir /opt/odoo/custom_addons/
        #rm /mnt/extra_addons/README.md
        #rm /mnt/extra_addons/LICENSE
        #rm /mnt/extra_addons/requirements.txt
      fi
    done
  fi
done
