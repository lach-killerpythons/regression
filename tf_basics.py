import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(2)
sesh =tf.Session()
result = tf.mul(x1, x2)
print(sesh.run(result))
sesh.close()