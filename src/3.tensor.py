import tensorflow as tf

x = tf.constant([100,200,300], name='x')

print(tf.rank(x))

y =tf.constant([1, 2, 3], name='y')

sum_x = tf.reduce_sum(x, name="sum_x")
prod_y = tf.reduce_prod(y, name="prod_y")
final_div = tf.div(sum_x, prod_y, name="final-div")

print(tf.rank(final_div))

final_mean = tf.reduce_mean([sum_x, prod_y], name="final_mean")

sess = tf.Session()

print(sess.run(x))
print(sess.run(y))
print(sess.run(sum_x))
print(sess.run(prod_y))
print(sess.run(final_mean))
print(sess.run(final_div))

writer= tf.summary.FileWriter("./m2_example4", sess.graph)
writer.close()
print(sess.close())


# usibn numpy in tensorflow

import numpy as np

sess = tf.Session()

zeroD = np.array(30, dtype=np.int32)
print(sess.run(tf.rank(zeroD)))
sess.close()