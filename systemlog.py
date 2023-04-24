import paramiko

#EC2 INSTANCE SSH CONNECTION
host = input("Enter Public IP of server")
username = input("Enter Username")
key_file = input("path to key.pem")

##SSH CLIENT TO LOAD KeyFile

ssh = paramiko.SSHClient
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=username, key_filename=key_file)


#CPU USAGE
stdin, stdout,stderr = ssh.exec_command('top -bn1 | grep "cpu" | sed "s/.",*\([0-9]*\)%* id.*/\\1/"')
cpu_usage= stdout.read().decode().strip


#DiskUsage
stdin, stdout, stderr = ssh.exec_command("df -h")
disk_usage= stdout.read().decode().strip().split('\n')[1].split()
total_d= disk_usage[1]
used_d = disk_usage[2]
free_d = disk_usage[3]

#MemoryUsage
stdin, stdout, stderr = ssh.exec_command("free -m")
mem_usage = stdout.read().decode().strip().split('\n')[1].split()
total_m=mem_usage[1]
used_m=mem_usage[2]
free_m=mem_usage[3]

#SysLogs
stdin, stdout, stderr = ssh.exec_command("sudo cat /var/log/syslog")
logs = stdout.read().decode()

#close connection
ssh.close




