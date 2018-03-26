import threading
import logging
import time


class TFProgress:
  def __init__(self, total_epoch_number=1, enable_print_progress_thread=False):
    self.current_progress = 0.0
    self.total_progress = 100.0

    self.current_batch_number = 0
    self.total_batch_number = 0
    self.current_epoch_number = 0
    self.total_epoch_number = total_epoch_number

    self.print_progress_interval = 1.0

    if enable_print_progress_thread:
      self.start_print_progress_thread()

  def print_progress(self):
    self.compute_current_progress()
    print("Progress: {}%".format(self.current_progress * 100))

  def set_total_epoch_number(self, epoch_number):
    self.total_epoch_number = epoch_number

  def increase_current_epoch_number(self):
    # TODO: Make this thread-safe for concurrent updating
    self.current_epoch_number += 1

  def clear_current_epoch_number(self):
    self.current_epoch_number = 0

  def set_print_progress_interval(self, print_progress_interval):
    self.print_progress_interval = print_progress_interval

  def compute_current_progress(self):
    self.current_progress = 1.0 * self.current_epoch_number / self.total_epoch_number

  def print_progress_thread(self):

    while True:

      self.print_progress()

      if self.current_progress == 1.0:
        print("The progress is done")
        return

      time.sleep(self.print_progress_interval)

  def start_print_progress_thread(self):
    logging.info("Start the new thread to periodically print progress")

    print_progress_thread = threading.Thread(
        target=self.print_progress_thread, args=())
    print_progress_thread.start()
    #print_progress_thread.join()
