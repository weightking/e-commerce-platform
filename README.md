# e-commerce-platform
This is a e-commerce-platform which the backend is developed based on django and the frontend developed based on the vue.

slave sql server start: mysql -uroot -pmysql -h 192.168.1.138 --port=8306 
slave sql connect with master sql: change master to master_host='192.168.1.138', master_user='slave', master_password='slave',master_log_file='mysql-bin.000006', master_log_pos=157;
show sql server id:show variables like 'server_id';
set sql server id: set global server_id=2;
show slave status:show slave status \G
docker run sql server: sudo docker run -p 8306:3306 --name mysql-slave -e MYSQL_ROOT_PASSWORD=mysql -d -v ~/mysql_slave/data:/var/lib/mysql -v ~/mysql_slave/mysql.conf.d:/etc/mysql/mysql.conf.d mysql:8.0.29
