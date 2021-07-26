#!/bin/bash
BATU=/usr/local/nginx/sbin/

#启动Nginx函数 
nginxstart(){
  ls $BATU/nginx &> /dev/null
  if [ "$?" -ne 0 ];then
	  echo "未安装nginx"
  elif [ $(ss -anput | grep nginx | wc -l) -eq 0 ] ;then
     $BATU/nginx
     if [ "$?" -eq 0 ] ;then
        echo "Nginx启动成功" 
     fi
  else
    echo "Nginx已启动服务,请勿重复启动此服务" 
   fi
}

#停止Nginx函数 
nginxstop(){
  if [ $(ss -anput | grep nginx | wc -l) -ne 0 ] ;then
     $BATU/nginx -s stop
    if [ "$?" -eq 0 ] ;then
      echo "Nginx停止成功" 
    fi
  else
      echo "Nginx已经停止服务,请勿重复停止此服务" 
  fi
}

#重新启动nginx服务
nginxrestart(){
    nginxstop &> /dev/null ;nginxstart &> /dev/null
    if [ $(ss -anput | grep nginx | wc -l) -ne 0 ] ;then
      echo "nginx服务重启成功"
    else
      echo "nginx服务重启失败"	 
    fi
}

#重新加载Nginx函数
nginxreload(){
  if [ $(ss -anput | grep nginx | wc -l) -ne 0 ] ;then
     $BATU/nginx -s reload
    if [ "$?" -eq 0 ] ;then
      echo "Nginx重新加载成功" 
    fi
  else
      echo "Nginx重新加载失败,未安装nginx或nginx服务已停止"
  fi
    #if [ "$?" -eq 0 ] ;then
    #  echo "Nginx重新加载成功" 
    # else
    # echo  "Nginx重新加载失败" 
    #fi
}

#检测配置文件语法错误Nginx函数
nginx_t(){
   ls $BATU/nginx &> /dev/null
   if [ "$?" -eq 0 ] ;then
      $BATU/nginx -t 
     if [ "$?" -eq 0 ] ;then
        echo "Nginx配置文件读取成功,successful" 
     else
        echo  "Nginx配置文件读取出现错误,failed" 
     fi
  else
     echo "未安装nginx" 
  fi
}


nginx_V(){
   ls $BATU/nginx &> /dev/null
   if [ "$?" -eq 0 ] ;then
      echo "查看Nginx版本信息如下:" 
      $BATU/nginx -V
   
  else
      echo  "查看Nginx版本信息failed,未安装nginx" 
  fi
}


echo "nginx启动|停止|重新加载|检测配置文件|查看Nginx版本信息请按以下执行,成功请按q退出"
echo "-------------------------------------------------------------------------------"
#echo "nginx启动|停止|重新加载|检测配置文件若出现失败,请按q退出,重新检查配置文件"
echo
echo
while :
do
read -p "start启动|stop停止|restart重启|reload重新加载|t检测配置文件|V查看Nginx版本信息:" key
echo "-------------------------------------------------------------------------------"
case $key in
start)
     nginxstart;;
stop)
     nginxstop;;
restart)
     #nginxstop
     #nginxstart;;
     nginxrestart;;
reload)
     nginxreload;;
t)
     nginx_t;;
V)
     nginx_V;;
q) 
     exit;;
*)
     echo "输入有误,请按照提示输入";;
esac
echo "-------------------------------------------------------------------------------"
echo "nginx服务若出现失败,请按q退出,重新检查配置文件!!!"
echo "###############################################################################"
echo
echo
done





