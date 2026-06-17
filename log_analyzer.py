log_file='sample.log'
try:
    with open(log_file,'r') as file:
        lines=file.readlines()
    total_requests=len(lines)

    print('log analysis report')
    print('total requests:',total_requests)
except FileNotFoundError:
    print('log file not found')