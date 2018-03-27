#!/usr/bin/env python

import time

from tf_progress.tf_progress import TFProgress


def main():

  epoch_number = 10

  #progress = TFProgress(total_epoch_number=epoch_number, enable_print_progress_thread=True, print_type=TFProgress.TYPE_PROGRESS_BAR)
  progress = TFProgress(
      total_epoch_number=epoch_number,
      enable_print_progress_thread=True,
      display_type=TFProgress.DISPLAY_TYPE_STDOUT_TEXT)

  for i in range(epoch_number):
    time.sleep(0.5)
    progress.increase_current_epoch_number()


if __name__ == "__main__":
  main()
