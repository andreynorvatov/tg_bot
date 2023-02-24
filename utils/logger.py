import logging

def initialize_log(file_name):
    cons_log_output = True
    if file_name:
        logging.basicConfig(filename=file_name,
                            format="%(asctime)-s %(levelname)-s [name: %(name)-s] [module: %(module)s] [process: %(process)s] [thread: %(thread)s] %(message)s",
                            # level = logging.DEBUG,
                            level=logging.INFO,
                            datefmt="%d.%m.%Y %H:%M:%S")
    if cons_log_output:
        cons_hnd = logging.StreamHandler()
        cons_hnd.setFormatter(logging.Formatter("%(asctime)s: %(levelname)s %(module)s - %(message)s", datefmt="%d.%m.%Y %H:%M:%S"))
        logging.getLogger().addHandler(cons_hnd)


initialize_log("LoadTest_Bot.log")
