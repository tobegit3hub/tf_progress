import threading
import logging
import time
import tqdm
import requests


class TFProgress:

  DISPLAY_TYPE_STDOUT_TEXT = 0
  DISPLAY_TYPE_STDOUT_BAR = 1
  DISPLAY_TYPE_LOCAL_FILE = 2
  DISPLAY_TYPE_HTTP_REQUEST = 3

  def __init__(self,
               total_epoch_number=1,
               enable_print_progress_thread=False,
               display_type=DISPLAY_TYPE_STDOUT_TEXT):
    self.current_progress = 0.0
    self.total_progress = 100.0

    self.current_batch_number = 0
    self.total_batch_number = 0
    self.current_epoch_number = 0
    self.total_epoch_number = total_epoch_number

    self.print_progress_interval = 1.0

    self.print_type = display_type

    if self.print_type == TFProgress.DISPLAY_TYPE_STDOUT_TEXT:
      pass
    elif self.print_type == TFProgress.DISPLAY_TYPE_STDOUT_BAR:
      self.tqdm_progress_bar = tqdm.tqdm()
    elif self.print_type == TFProgress.DISPLAY_TYPE_LOCAL_FILE:
      # TODO: Make this configurable
      progress_filename = "progress.txt"
      self.progress_file = open(progress_filename, "w")
    elif self.print_type == TFProgress.DISPLAY_TYPE_HTTP_REQUEST:
      # TODO: Make this configurable
      self.post_progress_url = "http://127.0.0.1:8000"

    if enable_print_progress_thread:
      self.start_print_progress_thread()

  def print_progress(self):
    self.compute_current_progress()

    if self.print_type == TFProgress.DISPLAY_TYPE_STDOUT_TEXT:
      print("Training progress: {}%".format(self.current_progress * 100))
    elif self.print_type == TFProgress.DISPLAY_TYPE_STDOUT_BAR:
      pass
    elif self.print_type == TFProgress.DISPLAY_TYPE_LOCAL_FILE:
      self.progress_file.seek(0, 0)
      self.progress_file.write("{}%".format(self.current_progress * 100))
      self.progress_file.flush()
    elif self.print_type == TFProgress.DISPLAY_TYPE_HTTP_REQUEST:
      self.post_progress_request()

  def get_current_progress(self):
    return self.current_progress

  def set_total_epoch_number(self, epoch_number):
    self.total_epoch_number = epoch_number

    if self.print_type == TFProgress.DISPLAY_TYPE_STDOUT_TEXT:
      pass
    elif self.print_type == TFProgress.DISPLAY_TYPE_STDOUT_BAR:
      self.tqdm_progress_bar.total = epoch_number
    elif self.print_type == TFProgress.DISPLAY_TYPE_LOCAL_FILE:
      pass
    elif self.print_type == TFProgress.DISPLAY_TYPE_HTTP_REQUEST:
      pass

  def increase_current_epoch_number(self):
    # TODO: Make this thread-safe for concurrent updating
    self.current_epoch_number += 1

    if self.print_type == TFProgress.DISPLAY_TYPE_STDOUT_TEXT:
      pass
    elif self.print_type == TFProgress.DISPLAY_TYPE_STDOUT_BAR:
      #self.tqdm_progress_bar.update(self.current_epoch_number)
      self.tqdm_progress_bar.update(1)
    elif self.print_type == TFProgress.DISPLAY_TYPE_LOCAL_FILE:
      pass
    elif self.print_type == TFProgress.DISPLAY_TYPE_HTTP_REQUEST:
      pass

  def clear_current_epoch_number(self):
    self.current_epoch_number = 0

  def set_print_progress_interval(self, print_progress_interval):
    self.print_progress_interval = print_progress_interval

  def compute_current_progress(self):
    self.current_progress = 1.0 * self.current_epoch_number / self.total_epoch_number

  def print_progress_thread(self):

    if self.print_type == TFProgress.DISPLAY_TYPE_STDOUT_BAR:
      # TODO: Need to intialize in this thread
      self.tqdm_progress_bar = tqdm.tqdm(total=self.total_epoch_number)

    while True:

      self.print_progress()

      if self.current_progress == 1.0:
        self.end_of_pregress()
        return

      time.sleep(self.print_progress_interval)

  def end_of_pregress(self):
    #print("The progress is done")

    if self.print_type == TFProgress.DISPLAY_TYPE_STDOUT_TEXT:
      pass
    elif self.print_type == TFProgress.DISPLAY_TYPE_STDOUT_BAR:
      self.tqdm_progress_bar.close()
    elif self.print_type == TFProgress.DISPLAY_TYPE_LOCAL_FILE:
      self.progress_file.close()
    elif self.print_type == TFProgress.DISPLAY_TYPE_HTTP_REQUEST:
      pass

  def start_print_progress_thread(self):
    logging.info("Start the new thread to periodically print progress")

    print_progress_thread = threading.Thread(
        target=self.print_progress_thread, args=())
    print_progress_thread.start()
    #print_progress_thread.join()

  def post_progress_request(self):
    payload = {"progress": self.current_progress}
    response = requests.post(self.post_progress_url, json=payload)
    # TODO: Check if request succeeds
    print("Request url: {} with data: {}".format(self.post_progress_url,
                                                 payload))
