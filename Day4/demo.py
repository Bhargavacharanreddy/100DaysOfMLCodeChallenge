import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()

a= tf.constant(10)
b= tf.constant(32)

print(sess.run(hello))


