firewall-cmd --permanent --add-port=10050/tcp 
firewall-cmd --permanent --add-port=10051/tcp 
firewall-cmd --permanent --add-port=80/tcp 
firewall-cmd --permanent --add-port=443/tcp 
firewall-cmd --permanent --add-port=10055/tcp
firewall-cmd --permanent --add-port=3306/tcp
firewall-cmd --reload 
