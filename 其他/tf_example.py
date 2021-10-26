#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2021-10-26

@author: Chant
tf.feature_column 示例
"""
import tensorflow as tf


def _vocab_list_embedding(key: str, vocab: list, embedding_dim: int, comb='mean'):
    vocabulary = tf.feature_column.categorical_column_with_vocabulary_list(key, vocab, num_oov_buckets=1)
    emb = tf.feature_column.embedding_column(vocabulary, dimension=embedding_dim, combiner=comb)
    return tf.keras.layers.DenseFeatures(emb)


data = {'a': [15, 9, 17, 19, 21, 18, 25, 30],
        'b': [5.0, 6.4, 10.5, 13.6, 15.7, 19.9, 20.3, 0.0],
        'c': list('abcd' * 2),
        'arr': [('11', '22',), ('11', '22'), ('33', '44'), ('22', '44')] * 2,
        # 序列维度必须一致，否则embedding会报错ValueError: Can't convert non-rectangular Python sequence to Tensor.
        # 'arr': [('11', '22',), ('11', '22','33'), ('33', '44'), ('22', '44')] * 2
        }
# 序列特征embedding
emb_arr = _vocab_list_embedding('arr', ['11', '22', '33', '44'], 3)
print(emb_arr(data))

a = tf.feature_column.numeric_column('a')
b = tf.feature_column.numeric_column('b')
# 分类特征embedding
c = tf.feature_column.categorical_column_with_vocabulary_list('c', list('abcd'))
emb_c = tf.feature_column.embedding_column(c, dimension=2, combiner='mean')
# 特征分箱
a_buckets = tf.feature_column.bucketized_column(a, boundaries=[10, 15, 20, 25, 30])
# 输出tensor
print(tf.keras.layers.DenseFeatures([a_buckets, b])(data))
print(tf.keras.layers.DenseFeatures([a_buckets, b, emb_c])(data))
print(tf.keras.layers.DenseFeatures(emb_c)(data))
# 特征交叉
cross_col = tf.feature_column.crossed_column([a_buckets, c], hash_bucket_size=1000)
emb_cross_col = tf.feature_column.embedding_column(cross_col, dimension=2, combiner='mean')
feature_layer = tf.keras.layers.DenseFeatures([emb_cross_col])
print(feature_layer(data))

columns = [cross_col]
features = tf.io.parse_example(data, features=tf.feature_column.make_parse_example_spec(columns))

# 另一种方式
t1 = tf.feature_column.embedding_column(
    tf.feature_column.categorical_column_with_hash_bucket("t1", 2), dimension=3)
t2 = tf.feature_column.numeric_column('t2')
feature_layer = tf.compat.v1.keras.layers.DenseFeatures([t1, t2])
features = {"t1": tf.constant(["a", "b"]), "t2": tf.constant([1, 2])}
dense_tensor = feature_layer(features, training=True)
print(dense_tensor)
