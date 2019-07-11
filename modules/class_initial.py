import os


class InputExample(object):
    """A single training/test example for simple sequence classification."""
    # 对简单序列分类的训练，定义了一个类InputExample
    def __init__(self, guid: object, text: object, label: object = None) -> object:
        """Constructs a InputExample.
        Args:
          guid: Unique id for the example.
          text_a: string. The untokenized text of the first sequence. For single
            sequence tasks, only this sequence must be specified.
          label: (Optional) string. The label of the example. This should be
            specified for train and dev examples, but not for test examples.
            :param guid:
            :param text:
            :param label:
        """

        self.guid = guid
        self.text = text
        self.label = label
        # 定义属性值