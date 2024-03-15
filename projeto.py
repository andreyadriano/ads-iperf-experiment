import subprocess
from time import sleep

alg = ['cubic','reno']
BER = ['1000000','100000']
e2e_delay = ['10000','100000'] # 10ms e 100ms
repeticao = 8

id_exp = 'i1234'

ip_pc1 = '10.0.0.20'
ip_pc2 = '10.0.2.20'
ip_pc3 = '10.0.3.20'
ip_pc4 = '10.0.4.20'


cmd_iperf_client="sudo himage pc1@" + id_exp + " iperf -c 10.0.0.21 -y C -Z " + alg[0] + " > dados-" + alg[0] + ".csv"

#para cada uma das repeticoes faca
for rep in range(repeticao):
    for protocolo in alg:
        for ber in BER:
            for e2e in e2e_delay:
                subprocess.run("sudo vlink -BER " + ber + " pc1:pc2@i3f30 ", shell=True)