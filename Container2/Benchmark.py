import os
import stat
import re

def prepare_exp(SSHHost, SSHPort, REMOTEROOT, optpt):
    f = open("config", 'w')
    f.write("Host benchmark\n")
    f.write("   Hostname %s\n" % SSHHost)
    f.write("   User ubuntu\n" )
    f.write("   Port %d\n" % SSHPort)
    f.close()
    

    f = open("run-experiment.sh", 'w')
    f.write("#!/bin/bash\n")
    f.write("set -x\n\n")
    
    f.write("sshpass -p ubuntu ssh -t -F config benchmark \"/usr/local/bin/memcached -d -u ubuntu -p 11211 -P /tmp/memcached.pid\"\n") # adjust this line to properly start memcached
    
    f.write("RESULT=`sshpass -p ubuntu ssh ubuntu@server \"pidof memcached\"`\n")

    f.write("sleep 5\n")

    f.write("if [ -z \"$RESULT\"]; then echo \"memcached process not running\"; CODE=1; else CODE=0; fi\n")
        
    f.write("mcperf --num-calls=%d --num-conns=%d --server=%s &> stats.log\n" % ( optpt["noRequests"], optpt["concurrency"], SSHHost)) #adjust this line to properly start the client
    
    f.write("REQPERSEC=`cat stats.log | grep -o 'Response rate: [0-9]\+\.[0-9]\+ ' | awk -F ': ' '{print $2}'`\n")
    
    f.write("LATENCY=`cat stats.log | grep -o 'Response time \[ms\]: avg [0-9]\+\.[0-9]\+ ' | awk -F ' ' '{print $5}'`\n")
    
    # add a few lines to extract the "Response rate" and "Response time \[ms\]: av and store them in $REQPERSEC and $LATENCY"
    
    f.write("ssh -F config benchmark \"sudo kill -9 $(cat memcached.pid)\"\n")

    f.write("echo \"requests latency\" > stats.csv\n")
    f.write("echo \"$REQPERSEC $LATENCY\" >> stats.csv\n")
    
    f.write("scp -F config benchmark:~/memcached.* .\n")

    f.write("if [[ $(wc -l <stats.csv) -le 1 ]]; then CODE=1; fi\n\n")
    
    f.write("exit $CODE\n")

    f.close()
    
    os.chmod("run-experiment.sh", stat.S_IRWXU) 
