import tensorflow as tf

# create a constant op that produces a 1x2 matrix.
# the op is added as a node to the default graph
# the value returned by the constructor is the output
# of the Constant operator (op)
m1 = tf.constant([[3., 3.]]) # note floats.

# another cosntant, 2x1 matrix
m2 = tf.constant([[2.], [2.]])


# matrix multiplication op that takes m1 and and m2,
# returned value, 'product', is the result of the matrix
# multiplication
product = tf.matmul(m1, m2)


# note: _no_ computation done yet! Just made a graph.

# default graph now has 3 nodes: two "constant" ops
# and one matrix multiplication (matmul) ops.
# to actually do the work, launch the graph in a session


# TIME TO ACTUALLY DO SOME COMPUTING!
# to run this graph (a matrix multiplication), we call run
# on the _product_, a rep of the matrix multiplication.
# this tells Tensorflow that we want the output of the
# matrix multiplication as our result.
# output of an op is a numpy `ndarray` object
with tf.Session() as session:
    result = session.run(product)
    print result
    # 'with' block implicitly closes the session. Neat!
