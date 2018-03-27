#!/usr/bin/env python

import time
import numpy as np
import tensorflow as tf

from tf_progress.tf_progress import TFProgress

# Prepare train data
train_X = np.linspace(-1, 1, 100)
train_Y = 2 * train_X + np.random.randn(*train_X.shape) * 0.33 + 10

# Define the model
X = tf.placeholder("float")
Y = tf.placeholder("float")
w = tf.Variable(0.0, name="weight")
b = tf.Variable(0.0, name="bias")

temp = tf.add(w, w)
loss = tf.square(Y - X * w - b)
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

epoch_number = 10
progress = TFProgress(
    total_epoch_number=epoch_number,
    enable_print_progress_thread=True,
    display_type=TFProgress.DISPLAY_TYPE_STDOUT_TEXT)

# Create session to run
with tf.Session() as sess:
  sess.run(tf.initialize_all_variables())

  epoch = 1
  for i in range(epoch_number):

    for (x, y) in zip(train_X, train_Y):
      _, w_value, b_value = sess.run([train_op, w, b], feed_dict={X: x, Y: y})

    print("Epoch: {}, w: {}, b: {}".format(epoch, w_value, b_value))
    epoch += 1

    time.sleep(1.5)
    progress.increase_current_epoch_number()
