class WashingMachine:
    def __init__(self):
        self.running = False
        self.cycletime = 0

    def start(self, cycletime):
        if not self.running:
            self.running = True
            self.cycletime = cycletime
            print("Washing machine started.")
            self.run()

    def pause(self):
        if self.running:
            self.running = False
            print("Washing machine paused.")

    def restart(self):
        if not self.running:
            self.running = True
            print("Washing machine resumed")
            self.run()

    def stop(self):
        if self.running:
            self.running = False
            print("Washing machine stopped.")

    def run(self):
        remaining_time = self.cycletime
        try:
            while self.running and remaining_time > 0:
                print("Time remaining in minutes:",remaining_time)
                remaining_time -= 1 
        except Exception as ex:
            print("Error",ex)
        finally:
            if self.running:
                print("Washing cycle completed")
                self.running = False


def main():
    washing_machine = WashingMachine()

    try:
        while True:
            print("Washing Machine steps:")
            print("1. Start")
            print("2. Pause")
            print("3. restart")
            print("4. Stop")
            n = input("Enter your choice:")
            if n == '1':
                cycletime = int(input("Enter cycle time in minutes:"))
                washing_machine.start(cycletime)
            elif n == '2':
                washing_machine.pause()
            elif n == '3':
                washing_machine.restart()
            elif n == '4':
                washing_machine.stop()
            elif n == '5':
                print("Exiting")
                break
            else:
                print("Invalid choice")
    except Exception as e:
        print("Error",e)
    finally:
        print("Cleaning up resource")

if __name__ == "__main__":
    main()
