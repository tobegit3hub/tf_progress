import threading
import logging
import time
import tqdm


class TFProgress:

  TYPE_PROGRESS_TEXT = 0
  TYPE_PROGRESS_BAR = 1

  def __init__(self,
               total_epoch_number=1,
               enable_print_progress_thread=False,
               print_type=TYPE_PROGRESS_TEXT):
    self.current_progress = 0.0
    self.total_progress = 100.0

    self.current_batch_number = 0
    self.total_batch_number = 0
    self.current_epoch_number = 0
    self.total_epoch_number = total_epoch_number

    self.print_progress_interval = 1.0

    self.print_type = print_type

    if self.print_type == TFProgress.TYPE_PROGRESS_TEXT:
      pass
    elif self.print_type == TFProgress.TYPE_PROGRESS_BAR:
      self.tqdm_progress_bar = tqdm.tqdm()

    if enable_print_progress_thread:
      self.start_print_progress_thread()

  def print_progress(self):
    self.compute_current_progress()

    if self.print_type == TFProgress.TYPE_PROGRESS_TEXT:
      print("Training progress: {}%".format(self.current_progress * 100))
    elif self.print_type == TFProgress.TYPE_PROGRESS_BAR:
      pass

  def get_current_progress(self):
    return self.current_progress

  def set_total_epoch_number(self, epoch_number):
    self.total_epoch_number = epoch_number

    if self.print_type == TFProgress.TYPE_PROGRESS_TEXT:
      pass
    elif self.print_type == TFProgress.TYPE_PROGRESS_BAR:
      self.tqdm_progress_bar.total = epoch_number

  def increase_current_epoch_number(self):
    # TODO: Make this thread-safe for concurrent updating
    self.current_epoch_number += 1

    if self.print_type == TFProgress.TYPE_PROGRESS_TEXT:
      pass
    elif self.print_type == TFProgress.TYPE_PROGRESS_BAR:
      #self.tqdm_progress_bar.update(self.current_epoch_number)
      self.tqdm_progress_bar.update(1)

  def clear_current_epoch_number(self):
    self.current_epoch_number = 0

  def set_print_progress_interval(self, print_progress_interval):
    self.print_progress_interval = print_progress_interval

  def compute_current_progress(self):
    self.current_progress = 1.0 * self.current_epoch_number / self.total_epoch_number

  def print_progress_thread(self):

    if self.print_type == TFProgress.TYPE_PROGRESS_BAR:
      # TODO: Need to intialize in this thread
      self.tqdm_progress_bar = tqdm.tqdm(total=self.total_epoch_number)

    while True:

      self.print_progress()

      if self.current_progress == 1.0:
        self.end_of_pregress()
        return

      time.sleep(self.print_progress_interval)

  def end_of_pregress(self):
    print("The progress is done")

    if self.print_type == TFProgress.TYPE_PROGRESS_TEXT:
      pass
    elif self.print_type == TFProgress.TYPE_PROGRESS_BAR:
      self.tqdm_progress_bar.close()

  def start_print_progress_thread(self):
    logging.info("Start the new thread to periodically print progress")

    print_progress_thread = threading.Thread(
        target=self.print_progress_thread, args=())
    print_progress_thread.start()
    #print_progress_thread.join()
