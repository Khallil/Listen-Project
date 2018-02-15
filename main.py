
import tensorflow as tf

filenames = ["/home/doudou/Documents/Listen-Project/audioset_v1_embeddings/0.tfrecord"]

def _parse_function(example_proto):
    features = {"video_id":tf.FixedLenFeature((), tf.bytes_list: )}

    }
    parsed_features = tf.parse_single_sequence_example(example_proto,)
    return parsed_features

dataset = tf.data.TFRecordDataset(filenames)
print "retour de TFRecordDataset : "
print dataset

dataset = dataset.map(_parse_function)
print dataset