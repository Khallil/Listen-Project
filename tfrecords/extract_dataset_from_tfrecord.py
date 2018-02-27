import tensorflow as tf

# we get an iterator for this file
reader = tf.python_io.tf_record_iterator('_0.tfrecord')
my_readed_example = [tf.train.SequenceExample().FromString(seq_example_str)
        for seq_example_str in reader]

y = list() #
x = list() #
# on prends que le premier seq_example
item = my_readed_example[0]
y = item.context.feature['labels'].int64_list.value
list_of_x = item.feature_lists.feature_list['audio_embedding'].feature
# on prends que la premiere seconde
x0 = list_of_x[4]
string =  str(x0.bytes_list.value)
bytes_128 = string.split('\\')
print len(bytes_128)