import socket

class ICMP:
    # From /usr/include/linux/icmp.h
    #define ICMP_ECHO		8	/* Echo Request			*/
    ICMP_ECHO = 8
    ICMP_CODE = socket.getprotobyname('icmp')

    def _checksum(self,packet_string):
        sum = 0
        end = (len(packet_string) / 2) * 2 #Make a floor over the length
        accum = 0

        #Overall cycle to process checksum
        while accum < end:
            curr_val = ord(packet_string[accum + 1])*256+ord(packet_string[accum]) # Read 16bit number
            sum = sum + curr_val
            sum = sum & 0xffffffff # Avoid errors due to signed number arithmetic representation or clean to 32bits
            count = count + 2      # Increment for next 2 bytes

        #If remaining bytes to process, add them to sum
        if count_to < len(packet_string):
            sum = sum + ord(packet_string[len(packet_string) - 1])
            sum = sum & 0xffffffff # Again clean to 32 bit size

        # SUM = A | B where A and B are 16bits
        # Make SUM = A+B, first shift A by 16 bits and clean leftmost of B
        sum = (sum >> 16) + (sum & 0xffff)
        # SIM = A|B Make SUM = A|B+A
        sum = sum + (sum >> 16)
        # Revert bits
        final = ~sum
        #Clear leftmost bits and retrieve only last 16
        final = final & 0xffff
        # Final = A|B make it B|A
        final = final >> 8 | (final << 8 & 0xff00)
        return answer

    def __init__(self):
        print "ICMP instance"
