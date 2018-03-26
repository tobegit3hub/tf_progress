
# TensorFlow Progress

## Introduction

Easy-to-use library for logging training progress of TensorFlow.

## Usage

```
progress = TFProgress(total_epoch_number=10, enable_print_progress_thread=True)

for i in range(10):
  progress.increase_current_epoch_number()
```

![](./screenshot.png)