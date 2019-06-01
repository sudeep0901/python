import tensorflow as tf
# y =Wx + b
W = tf.constant([10, 100], name="const_W")

x=tf.placeholder(tf.int32, name='x')
b=tf.placeholder(tf.int32, name='b')

Wx = tf.multiply(W, x, name="Wx")

y = tf.add(Wx, b, name='y')

y_ = tf.subtract(x, b, name="y_")
with tf.Session() as sess:
    print("Intermediate Result: Wx = ", sess.run(Wx, feed_dict={x:[3, 33]}))
    print("Final Result: Wx + b = ", sess.run(y, feed_dict={x:[5, 50], b:[7, 9]}))
    print("Intermediate Result: Wx + b = ", sess.run(fetches=y, feed_dict={Wx:[100, 1000], b:[7, 9]}))
    print("Intermediate Result: Wx + b = ", sess.run(fetches=[y, y_], feed_dict={x:[100, 1000], b:[7, 9]}))
    writer = tf.summary.FileWriter('./m3_example6', sess.graph)
    writer.close()
