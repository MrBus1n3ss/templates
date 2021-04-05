class CiscoLogin:
    def __init__(self, ip_address):
        self.user_name = getpass.getuser()
        self.exspawn = ''
        self.display_list = []
        self.ip_address = ip_address
        if "PASS" in os.environ:
            self.password = os.environ['PASS']
        else:
            self.password = ''


    def cisco_ssh_login(self, termLen0=True, showLog=False):
        if self.ip_address == '' or self.password == '':
            return False
        try:
            self.exspawn = pexpect.spawn(
                "ssh "
                + str(self.user_name)
                + "@"
                + str(self.ip_address), encoding='utf-8'
            )
            self.exspawn.setwinsize(100, 400)
            if showLog:
                self.exspawn.logfile = sys.stdout
        except Exception:
            return False

        index = 0
        while not index == 3:

            try:
                index = self.exspawn.expect(["no\)\?", "assword:", ">", "#"])
                if index == 0:
                    self.exspawn.sendline("yes")
                    self.exspawn.expect("yes")
                    time.sleep(0.5)
                if index == 1:
                    self.exspawn.logfile = None
                    self.exspawn.sendline(self.password)
                    self.exspawn.expect("")
                    time.sleep(1)
                if index == 2:
                    if showLog:
                        self.exspawn.logfile = sys.stdout
                    self.exspawn.sendline("en")
                    self.exspawn.expect("en")
                    time.sleep(0.5)
                if index == 3:
                    self.exspawn.sendline("")
                    break
            except Exception as ex:
                print("Unable to SSH/Login/Authenticate: " + str(self.ip_address))
                return False
        if termLen0:
            try:
                self.exspawn.expect("#")
                self.exspawn.sendline("terminal length 0")
                self.exspawn.sendline("")
            except Exception:
                return False

    def interact(self):
        self.exspawn.interact()

    def send_line(self, command, commandTimeout=30, simple=False):
        try:
            self.exspawn.expect("#")
            self.exspawn.sendline(command)
            self.exspawn.expect(command)
        except Exception:
            return False
        # -------------------------
        if ("ping" in command) or simple:
            # -------------------------
            try:
                self.exspawn.expect("#", timeout=commandTimeout)
                commandOutput = str(self.exspawn.before)
                self.exspawn.sendline("")
            except Exception:
                return False
            # -------------------------
        else:
            # -------------------------
            try:
                self.exspawn.sendline("")
                self.exspawn.expect("#\r", timeout=commandTimeout)
                commandOutput = str(self.exspawn.before)
                self.display_list.append(commandOutput)
            except Exception:
                return False
            # -------------------------

    def logout(self):
        try:
            self.exspawn.expect("#")
            self.exspawn.sendline("~.")
        except Exception:
            return False
        self.exspawn.close()
        return True
