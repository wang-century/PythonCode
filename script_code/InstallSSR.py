""" 安装ssr与bbr脚本 """
import os

def install_ssr():
    os.system('wget --no-check-certificate -O shadowsocks-all.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-all.sh')
    os.system('chmod +x shadowsocks-all.sh')
    os.system('./shadowsocks-all.sh 2>&1 | tee shadowsocks-all.log')
    
def install_bbr():
    os.system('wget --no-check-certificate -O tcp.sh https://github.com/cx9208/Linux-NetSpeed/raw/master/tcp.sh && chmod +x tcp.sh && ./tcp.sh')

if __name__ == "__main__":
    choice = input('请选择要安装的内容：\n1.SSR\n2.BBR加速')
    if choice == '1':
        install_ssr()
    elif choice == '2':
        install_bbr()
    else:
        print('请输入正确的选项！')