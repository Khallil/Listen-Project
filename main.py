
import tensorflow as tf

# On lit le fichier et on le transforme en objet Example
reader = tf.python_io.tf_record_iterator('/home/doudou/Documents/Listen-Project/tfrecords/_0.tfrecord')
my_readed_examples = [tf.train.SequenceExample().FromString(example_str)
        for example_str in reader]

#my_n_example=my_readed_examples[0]
for seq_example in my_readed_examples:
    print seq_example