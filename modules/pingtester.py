import datetime, time, requests
class Ping:
    timevalues = {
        0: "ч.",
        1: "м.",
        2: "с",
    }
    def pingTester(self, ctime):
        self.colon = 0
        requests.get('https://google.com')
        f = str(datetime.datetime.now() - ctime)
        for i in range(len(f)):
            if f[i] == ':':
                self.colon += 1
                if int(f[i+1]) > 0:
                    return f[i+1:i+3]
                if int(f[i-1]) > 0:
                    return f[i-1]
            elif f[i] != '.':
                if int(f[i]) > 0:
                    f = f.split(":")[self.colon].replace('00', '0')
                    for k in range(len(f)):
                        if f[k] == ".":
                            return f"{f[k-1:k+3]}{self.timevalues[self.colon]}"
            elif f[i] != ':' and f[i] != '.':
                if int(f[i]) > 0:
                    return f"{f[i:i+1]}{self.timevalues[i]}"