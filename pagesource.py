def get_ticket_status(ticket_num, ticket_desc_str, e1):
    status_ticketnum_count = ticket_desc_str.count(ticket_num)
    if(status_ticketnum_count == 1):
        status_startpos = ticket_desc_str.index(ticket_num,0,len(ticket_desc_str))
        endpos = status_startpos

        e = 3
        while(e != 0):
            status_endpos = ticket_desc_str.index('</span>',endpos+3,len(ticket_desc_str))
            endpos = status_endpos + 3
            e -= 1
    #        app_logger.info("end position of Status*+ is " , status_startpos)
    #        app_logger.info("end position of Status*+ is " , status_endpos , "\n")

        status_str = ticket_desc_str[status_startpos:status_endpos]
        status = status_str.split('">')[-1]
    else:
        endpos = 0
        e = 2
        while(e != 0):
            status_startpos = ticket_desc_str.index(ticket_num,endpos,len(ticket_desc_str))
            endpos = status_startpos + 3
            e -= 1

        e1 = e1
        endpos = status_startpos
        while(e1 != 0):
            status_endpos = ticket_desc_str.index('</span>',endpos+3,len(ticket_desc_str))
            endpos = status_endpos + 3
            e1 -= 1

        status_str = ticket_desc_str[status_startpos:status_endpos]
        status_str = ticket_desc_str[status_startpos:status_endpos]
        
        # ticket_desc
        status = status_str.split('">')[-1]
        status = status.strip('\n').strip().lower()

    return status
def get_ticket_details(ticket_num, ticket_desc_str, pos):
    
    status_ticketnum_count = ticket_desc_str.count(ticket_num)
    if(status_ticketnum_count == 1):
        status_startpos = ticket_desc_str.index(ticket_num,0,len(ticket_desc_str))
        endpos = status_startpos

        e = 3
        while(e != 0):
            status_endpos = ticket_desc_str.index('</span>',endpos+3,len(ticket_desc_str))
            endpos = status_endpos + 3
            e -= 1
    #        app_logger.info("end position of Status*+ is " , status_startpos)
    #        app_logger.info("end position of Status*+ is " , status_endpos , "\n")

        status_str = ticket_desc_str[status_startpos:status_endpos]
        status = status_str.split('">')[-1]
    else:
        endpos = 0
        e = 2
        while(e != 0):
            status_startpos = ticket_desc_str.index(ticket_num,endpos,len(ticket_desc_str))
            endpos = status_startpos + 3
            e -= 1

        e = pos
        endpos = status_startpos
        while(e != 0):
            status_endpos = ticket_desc_str.index('</span>',endpos+3,len(ticket_desc_str))
            endpos = status_endpos + 3
            e -= 1

        # ticket_elements_str = ticket_desc_str[status_startpos:status_endpos]
        ticket_elements_str = ticket_desc_str[status_startpos:status_endpos]
        
        # ticket_desc
        ticket_elements = ticket_elements_str.split('">')[-1]
        ticket_elements = ticket_elements.strip('\n').strip().lower()

    return ticket_elements


f = open('pagesource.txt', 'r')
ticket_details = f.read()
ticket_details
e1 =7
print("Priority")
print(get_ticket_details('INCC00008570697', ticket_details, e1), e1)
print("assigned group")
e1 =8
print(get_ticket_details('INCC00008570697', ticket_details, e1), e1)
e1 =9
print("assigned to")
print(get_ticket_details('INCC00008570697', ticket_details, e1), e1)

e1 = 2
while(True):
    print(get_ticket_details('INCC00008570697', ticket_details, e1), e1)
