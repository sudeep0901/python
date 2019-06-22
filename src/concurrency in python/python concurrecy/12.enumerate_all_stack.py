def UpDataShare():
    thread = []
    MaxThread = 3
    num=0
    code = Tools().GetShareCode()
    for x in code:
        y = threading.Thread(target=ChildThead, args=(x,))
        thread.append(y)
    try:
        for t in tqdm(thread):
            t.start()
            while True:
                time.sleep(0.05)
                if len(threading.enumerate()) < MaxThread:
                    if len(code) - num < 13:
                        t.join()
                    num = num + 1
                    break
    except:
        print "1223" 
