
# TensorFlow Progress

## Introduction

Easy-to-use library for logging training progress of TensorFlow.

## Usage

```
from tf_progress import TFProgress

progress = TFProgress(total_epoch_number=10, enable_print_progress_thread=True)

for i in range(10):
  progress.increase_current_epoch_number()
```

![](./screenshot.png)

## APIs

Initialize the TFProgress object.

```
progress = TFProgress(total_epoch_number=10, enable_print_progress_thread=True)
```

Set the total epoch number.

```
progress.set_total_epoch_number(10)
```

Update the current epoch number.

```
progress.increase_current_epoch_number()

progress.set_current_epoch_number(10)

progress.clear_current_epoch_number()
```

Print the progress status.

```
print(progress.get_current_progress())

progress.print_progress()

progress.start_print_progress_thread()
```
