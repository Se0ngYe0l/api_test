import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

ssh.connect(hostname = "223.195.34.211", username='seongyeol', password='1230')

ssh.close()