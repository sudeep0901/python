import tensorflow as tf

A = tf.constant([4], tf.int32, name='A')
B = tf.constant([4], tf.int32, name='B')
C = tf.constant([4], tf.int32, name='C')

x = tf.placeholder(tf.int32, name='x')

with tf.name_scope("Equation_1"):
    AX2_1 = tf.multiply(A, tf.pow(x,2), name='AX2_1')
    Bx = tf.multiply(B, tf.pow(x,2), name='Bx')
    # Cx = tf.add_n(C, tf.pow(x,2), name='Cx')

    y1 = tf.add_n([AX2_1, Bx, C], name="y1")

with tf.name_scope("Equation_1"):
    AX2_2 = tf.multiply(A, tf.pow(x,2), name='AX2_2')
    Bx2 = tf.multiply(B, tf.pow(x,2), name='Bx2')
    # Cx = tf.add_n(C, tf.pow(x,2), name='Cx')

    y2 = tf.add_n([AX2_1, Bx, C], name="y2")

with tf.name_scope("Result"):
    y = y1 + y2

with tf.Session() as sess:
    print(sess.run(y,feed_dict={x:[10]}))
    writer =tf.summary.FileWriter('./m3_example7', sess.graph)
    writer.close()


