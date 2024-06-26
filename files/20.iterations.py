# Iterations and Comprehensions
# used to process multiple items or repeat tasks
# 1. Iteration Protocol
# An iterable is any object that can return its members one at a time.
# Example (checking server status):
servers = ['web1', 'web2', 'web3', 'db1', 'cache1']
for server in servers:
    print(f"Checking status of {server}")

# 2. List Comprehensions
# Example (filtering log files)
log_files = ['app.log', 'error.log', 'access.log', 'debug.log', 'system.log']
# Get only the log files starting with 'a' or 'e'
important_logs = [log for log in log_files if log.startswith(('e', 'a'))]
print(f"Important logs to check: {important_logs}")

# 3. Dictionary Comprehensions
# Example (creating a server status dictionary)
servers = ['web1', 'web2', 'web3', 'db1', 'cache1']
# Assure that all servers are 'online'
server_status = {server: 'online' for server in servers}
print(server_status)


# 4. Generator Expression
# Example (processing large log files)
def get_error_lines(logfile):
    return (line for line in open(logfile) if 'ERROR' in line)


for error in get_error_lines('app.log'):
    print(f"Found error: {error.strip()}")

# 5. enumerate() function
# Example (numbered task list)
deployment_steps = ['Stop service', 'Backup Data', 'Update code', 'Run migrations', 'Start service']
for step_num, step in enumerate(deployment_steps, start=1):
    print(f"Step {step_num}: {step}")

# 6. zip() function
# Example (pairing servers with their IP addresses)
severs = ['web1', 'web2', 'web3', 'db1', 'cache1']
ip_addresses = ['192.168.1.10', '192.168.1.20', '192.168.1.30', '192.168.1.40', '192.168.1.50']
for server, ip in zip(servers, ip_addresses):
    print(f"Server {server} has IP address {ip}")

