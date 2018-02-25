import tensorflow as tf

# we get an iterator for this file
reader = tf.python_io.tf_record_iterator('_0.tfrecord')
my_readed_example = [tf.train.SequenceExample().FromString(seq_example_str)
        for seq_example_str in reader]

y = list() #
x = list()
for item in my_readed_example:
    # get the label(s)
    y.append(item.context.feature['labels'].int64_list.value)
    # get the bytes 0 1 2 3 4 5 6 7 8 9 
    list_of_x = item.feature_lists.feature_list['audio_embedding'].feature
    for _x in list_of_x:
        _x.bytes_list.value