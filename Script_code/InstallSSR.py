import os

def install_ssr():
    os.system('wget --no-check-certificate -O shadowsocks-all.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-all.sh')
    os.system('chmod +x shadowsocks-all.sh')
    os.system('./shadowsocks-all.sh 2>&1 | tee shadowsocks-all.log')
    
def install_bbr():
    os.system('wget --no-check-certificate -O tcp.sh https://github.com/cx9208/Linux-NetSpeed/raw/master/tcp.sh && chmod +x tcp.sh && ./tcp.sh')

if __name__ == "__main__":
    install_ssr()
    install_bbr()