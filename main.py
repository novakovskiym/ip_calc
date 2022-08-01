# Simple IP calculator
# by Maksym Novakovskyi
# version 0.2

#Add '.' to binary
def ip_format_bin(unf_str: str):
    output_str: str = unf_str[0:8] + '.' + \
                      unf_str[8:16] + '.' + \
                      unf_str[16:24] + '.' + \
                      unf_str[24:]
    return output_str


#Convert bin to dec by octets
def ip_bin_to_dec(unc_str: str):
    output_str = str(int(unc_str[0:8], 2)) + '.' + \
                 str(int(unc_str[8:16], 2)) + '.' + \
                 str(int(unc_str[16:24], 2)) + '.' + \
                 str(int(unc_str[24:], 2))
    while len(output_str) < 15:
        output_str = output_str + ' '
    return output_str


def get_full_ip():
    full_ip = input('Please enter an IP Address: ')
    try:
        parts1 = full_ip.split('/')
        if len(parts1) == 2:
            ip_part = parts1[0]
            parts2 = ip_part.split('.')
            if len(parts2) == 4 and \
                all(0 <= int(part) <= 255 for part in parts2):
                return full_ip
            else:
                print('Invalid IP Address!!!')
                exit()
        else:
            print('No mask provided!!!')
            exit()
    except ValueError:
        return False
    except (AttributeError, TypeError):
        return False

#Get initial data (WIP)

ip: str = get_full_ip()
if not ip:
    exit()
split_str = ip.split('/')
ip_str = split_str[0]
mask_str = split_str[1]
ip_split_str = ip_str.split('.')


#IP Address
bin_ip: str = ''
for octet in ip_split_str:
    temp = str(bin(int(octet)))[2:]
    while temp.__len__() < 8:
        temp = '0' + temp
    bin_ip += temp

#IP Mask
bin_mask: str = ''
while bin_mask.__len__() < 32:
    if bin_mask.__len__() < int(mask_str):
        bin_mask += '1'
    else:
        bin_mask += '0'


#Network Address
net_addr = bin_ip[:bin_mask.count('1')]
while net_addr.__len__() < 32:
    net_addr += '0'

#Broadcast
bc_addr = bin_ip[:bin_mask.count('1')]
while bc_addr.__len__() < 32:
    bc_addr += '1'


#First IP
first_addr = bin_ip[:bin_mask.count('1')]
while first_addr.__len__() < 32:
    first_addr += '0'
first_addr = first_addr[:-1] + '1'

#Last IP
last_addr = bin_ip[:bin_mask.count('1')]
while last_addr.__len__() < 32:
    last_addr += '1'
last_addr = last_addr[:-1] + '0'


#Total Hosts
max_hosts = int(last_addr, 2) - int(first_addr, 2) + 1

print(f'IP Addr:\t\t{ip_bin_to_dec(bin_ip)}\t({ip_format_bin(bin_ip)})')
print(f'IP Mask:\t\t{ip_bin_to_dec(bin_mask)}\t({ip_format_bin(bin_mask)})')
print(f'Net Addr:\t\t{ip_bin_to_dec(net_addr)}\t({ip_format_bin(net_addr)})')
print(f'BC Addr:\t\t{ip_bin_to_dec(bc_addr)}\t({ip_format_bin(bc_addr)})')
print(f'First IP:\t\t{ip_bin_to_dec(first_addr)}\t({ip_format_bin(first_addr)})')
print(f'Last IP:\t\t{ip_bin_to_dec(last_addr)}\t({ip_format_bin(last_addr)})')
print(f'Total hosts:\t{str(max_hosts)}')
