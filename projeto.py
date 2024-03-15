import subprocess
from time import sleep

alg = ['cubic','reno']
BER = ['1000000','100000']
e2e_delay = ['10000','100000'] # 10ms e 100ms
repeticao = 8

id_exp = 'i234'
exec_time = '200'
server_exec_time = '50'

ip_pc1 = '10.0.0.20'
ip_pc2 = '10.0.2.20'
ip_pc3 = '10.0.3.20'
ip_pc4 = '10.0.4.20'

bandas = ['500000kbps','700000kbps']

# Comandos

# Inicia o imunes
inicia_imunes = ['sudo', 'imunes', '-b', '-e', id_exp, 'projeto.imn']

# Tráfego background uDP
init_iperf_server_udp = ['sudo', 'himage', 'pc3@'+id_exp, 'iperf', '-s', '-u'] # inicia como server e usa UDP
init_iperf_client_udp = ['sudo', 'himage', 'pc4@'+id_exp, 'iperf', '-c', ip_pc3, '-u', '-t', server_exec_time, '-b'] # inicia como cliente e usa UDP

# Tráfego background TCP
init_iperf_server_tcp = ['sudo','himage', 'pc1@'+id_exp, 'iperf', '-s'] # inicia como server e usa TCP

subprocess.Popen(inicia_imunes).wait()
subprocess.Popen('cleanupAll').wait()

#para cada uma das repeticoes faca
# for rep in range(repeticao):
#     for protocolo in alg:
#         for ber in BER:
#             for e2e in e2e_delay:
#                 # subprocess.run("sudo vlink -BER " + ber + " pc1:pc2@" + id_exp, shell=True)
#                 subprocess.Popen(inicia_imunes).wait()