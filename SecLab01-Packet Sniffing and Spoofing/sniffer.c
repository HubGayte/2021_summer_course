#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pcap/pcap.h>
#include <net/ethernet.h>
#include <netinet/ip.h>


/* This function will be invoked by pcap for each captured packet.
We can process each packet inside the function.
*/
void got_packet(u_char *args, const struct pcap_pkthdr *header, const u_char *packet){
    //printf("Got a packet\n");
    printf("Received a packet!\n");
    struct ether_header *eth = (struct ether_header*)packet;

    if(ntohs(eth->ether_type) == 0x800)
    {
        struct ip *ip1 = (struct ip *)(packet + sizeof(struct ether_header));
        printf("From : %s\n", inet_ntoa(ip1->ip_src));
        printf("To : %s\n", inet_ntoa(ip1->ip_dst));

        switch(ip1->ip_p)
        {
            case 6:
                printf("Protocol : TCP\n");
                break;

            case 17:
                printf("Protocol : UDP\n");
                break;

            case 1:
                printf("Protocol : ICMP\n");
                break;

            default:
                printf("Protocol : Others\n");
                break;
        }
  }
}

int main(){
    pcap_t *handle;
    char errbuf[PCAP_ERRBUF_SIZE];
    struct bpf_program fp;
    char filter_exp[] = "ip proto icmp";
    bpf_u_int32 net;
    // Step 1: Open live pcap session on NIC with name ethx
    // you need to change "eth3" to the name
    // found on their own machines (using ifconfig).
    
    handle = pcap_open_live("br-d3a9c727d803", BUFSIZ, 1, 1000, errbuf);

    if (handle == NULL) {
        fprintf(stderr, "Can't open eth3: %s\n", errbuf);
        exit(1);
    }
    // Step 2: Compile filter_exp into BPF psuedo-code
    
    pcap_compile(handle, &fp, filter_exp, 0, net);
    //pcap_setfilter(handle, &fp);
    
    // Step 3: Capture packets
    pcap_loop(handle, -1, got_packet, NULL);
    pcap_close(handle); //Close the handle
    
    return 0;
}
// Note: don't forget to add "-lpcap" to the compilation command.
// For example: gcc -o sniffer sniffer.c -lpcap

// Network device: br-d3a9c727d803
