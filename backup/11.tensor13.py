import tensorflow as tf
import numpy as np

# print(tf.__file__)

a = tf.constant(6.5, name='constant_a')
b = tf.constant(3.4, name='constant_b')
c = tf.constant(3.0, name='constant_c')
d = tf.constant(100.2, name='constant_d')

square = tf.square(a, name='constant_a')
power = tf.pow(b,c, name="pow_b_c")
sqrt = tf.sqrt(d, name="sqrt_d")
print(square)

final_sum = tf.add_n([square, power, sqrt], name ='final_sum')

sess = tf.Session()

print("Squar of a:", sess.run(square))
print("power of bc:", sess.run(power))
print("sqrt of d:", sess.run(sqrt))
print("final:", sess.run(final_sum))


writer =tf.summary.FileWriter("./m2_example2", sess.graph)

writer.close()
sess.close()
