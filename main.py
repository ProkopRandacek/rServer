import requestHandler, sys, traceback, time
from log import log

fastErrorCount = 0
lastErrorTime = 0

def main(args):
    if args == []:
        pass
    elif args == ["--debug"]:
        #TODO
        log("Debug log enabled")
    else:
        log(f"Unknown argument \"{args[0]}\"")
        exit()
    log("Starting webserver")
    requestHandler.start()

if __name__ == "__main__":
    while True:
        try:
            if len(sys.argv) > 0:
                main(sys.argv[1:])
            else:
                main([])
        except KeyboardInterrupt:
            log("KeyboardInterrupt")
            break
        except Exception:
            log("Error:\n" + traceback.format_exc())
            if time.time() - lastErrorTime < 10:
                fastErrorCount += 1
            else:
                fastErrorCount = 0
            if fastErrorCount > 6:
                log("Too many error in the past 60 seconds")
                break
            lastErrorTime = time.time()
            
        log("Trying to restart")
    log("Exiting")
