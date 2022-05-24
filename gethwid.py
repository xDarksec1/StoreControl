import subprocess


if __name__ == "__main__":
    try:
        hwid = (
            str(subprocess.check_output("wmic csproduct get uuid"), "utf-8")
            .split("\n")[1]
            .strip()
        )
        print(hwid)
    except BaseException:
        import sys

        print(sys.exc_info()[0])
        import traceback

        print(traceback.format_exc())
    finally:
        print("Press Enter to continue ...")
        input()
