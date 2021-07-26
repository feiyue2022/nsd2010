#!/bin/bash
##本脚本使用之前请检查你的光盘镜像是否完整，yum仓库设置是否正确
#本机IP
ipadd=`ifconfig ens33  | awk '/inet /{print $2}'`
#子网掩码
DHCPmask=`ifconfig ens33  | awk '/inet /{print $4}'`
#网段
DHCPnet=`echo ${ipadd%.*}.0`
#DHCP地址池最小值
DHCPmin=`echo ${ipadd%.*}.100`
#DHCP地址池最大值
DHCPmax=`echo ${ipadd%.*}.200`
#下一跳
next_server=`ifconfig ens33  | awk '/inet /{print $2}'`
#HTTP服务地址
HTTP_IP=`echo ${ipadd}`
#网关
router=`route -n | awk '/^[0.0.0.0]/{print $2}'`


##########################################



#DHCPnet=192.168.4.0
#网段
#DHCPmask=255.255.255.0
#子网掩码
#DHCPmin=192.168.4.110
#DHCP地址池最低ip
#DHCPmax=192.168.4.200
#dhcp最大IP
#router=192.168.4.1
#网关
#next_server=192.168.4.100
#吓一跳
#HTTP_IP=192.168.4.100
#HTTP服务地址
##关闭selinux和防火墙
setenforce 0
systemctl stop firewalld

##安装软件包
yum -y install httpd dhcp tftp-server syslinux
#syslinux 是为了cp pxelinux.0 这个二进制文件

##配置dhcp服务
cat > /etc/dhcp/dhcpd.conf << EOF

subnet $DHCPnet netmask $DHCPmask {
   range $DHCPmin $DHCPmax;
   option routers $router;
   default-lease-time 600;
   max-lease-time 7200;
   next-server $next_server;
   filename "pxelinux.0";
}
EOF
systemctl start dhcpd
systemctl enable dhcpd
##配置http共享光盘服务
[ ! -e /dev/cdrom ] && exit
[ -d /var/www/html/dvd ] || mkdir /var/www/html/dvd
mount /dev/cdrom /var/www/html/dvd/
systemctl restart httpd
##配置kickstart文件
cat > /var/www/html/ks.cfg << EOF
install
keyboard 'us'
rootpw --plaintext 1
url --url="http://$HTTP_IP/dvd/"
lang en_US
firewall --disabled
auth --useshadow --passalgo=sha512
text
selinux --disabled
skipx
network --bootproto=dhcp --device=eth0
reboot
timezone Asia/Shanghai
bootloader --location=mbr
zerombr
clearpart --all --initlabel
part /boot --fstype="xfs" --size=500
part / --fstype="xfs" --grow --size=1
%packages
@base
@network-file-system-client
@network-tools
%end
EOF
##配置tftp
cp /usr/share/syslinux/pxelinux.0 /var/lib/tftpboot/
cp /var/www/html/dvd/isolinux/* /var/lib/tftpboot
[ -d /var/lib/tftpboot/pxelinux.cfg ]  || mkdir /var/lib/tftpboot/pxelinux.cfg/
cat > /var/lib/tftpboot/pxelinux.cfg/default << EOF
default vesamenu.c32
timeout 20

label linux
  menu label ^Install CentOS 7
  Kernel vmlinuz
  append initrd=initrd.img ks=http://$HTTP_IP/ks.cfg
EOF
systemctl start tftp

iptables -F








