import tensorflow as tf

# variable w/ inital zero value
counter = tf.Variable(0, name="counter")

# create an op to increment the counter
inc_value = tf.constant(10)
update = tf.assign(counter, tf.add(counter, inc_value))

# variables have to be initialized after we have launched the graph
init_op = tf.initialize_all_variables()

with tf.Session() as session:
    # init:
    session.run(init_op)

    # initial value
    print session.run(counter)

    for _ in range(10):
        session.run(update)
        print session.run(counter)
