#   Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
import unittest
import numpy as np
import paddle
from tests.op_test import OpTest

paddle.enable_static()


class TestScatterOp(OpTest):
    def setUp(self):
        self.op_type = "scatter"
        self.place = paddle.CustomPlace("mlu", 0)
        self.__class__.use_custom_device = True
        self.python_api = paddle.scatter
        ref_np = np.ones((3, 50)).astype("float32")
        index_np = np.array([1, 2]).astype("int32")
        updates_np = np.random.random((2, 50)).astype("float32")
        output_np = np.copy(ref_np)
        output_np[index_np] = updates_np
        self.inputs = {"X": ref_np, "Ids": index_np, "Updates": updates_np}
        self.outputs = {"Out": output_np}

    def test_check_output(self):
        self.check_output_with_place(self.place, check_eager=False)

    def test_check_grad(self):
        self.check_grad(["X", "Updates"], "Out", check_eager=False)


class TestScatterOp0(OpTest):
    def setUp(self):
        self.op_type = "scatter"
        self.place = paddle.CustomPlace("mlu", 0)
        self.__class__.use_custom_device = True
        self.python_api = paddle.scatter
        ref_np = np.ones((3, 3)).astype("float32")
        index_np = np.array([1, 2]).astype("int32")
        updates_np = np.random.random((2, 3)).astype("float32")
        output_np = np.copy(ref_np)
        output_np[index_np] = updates_np
        self.inputs = {"X": ref_np, "Ids": index_np, "Updates": updates_np}
        self.attrs = {"overwrite": True}
        self.outputs = {"Out": output_np}

    def test_check_output(self):
        self.check_output_with_place(self.place, check_eager=False)

    def test_check_grad(self):
        self.check_grad(["X", "Updates"], "Out", check_eager=False)


class TestScatterOp1(OpTest):
    def setUp(self):
        self.op_type = "scatter"
        self.place = paddle.CustomPlace("mlu", 0)
        self.__class__.use_custom_device = True
        self.python_api = paddle.scatter
        ref_np = np.ones((3, 3)).astype("float32")
        zeros_np = np.zeros([2, 3]).astype("float32")
        index_np = np.array([1, 1]).astype("int32")
        updates_np = np.random.random((2, 3)).astype("float32")
        output_np = np.copy(ref_np)
        output_np[index_np] = zeros_np
        for i in range(0, len(index_np)):
            output_np[index_np[i]] += updates_np[i]
        self.attrs = {"overwrite": False}
        self.inputs = {"X": ref_np, "Ids": index_np, "Updates": updates_np}
        self.outputs = {"Out": output_np}

    def test_check_output(self):
        self.check_output_with_place(self.place, check_eager=False)

    def test_check_grad(self):
        self.check_grad(["X", "Updates"], "Out", check_eager=False)


class TestScatterOp2(OpTest):
    def setUp(self):
        self.op_type = "scatter"
        self.place = paddle.CustomPlace("mlu", 0)
        self.__class__.use_custom_device = True
        self.python_api = paddle.scatter
        ref_np = np.ones((3, 3)).astype("float32")
        index_np = np.array([1, 2]).astype("int64")
        updates_np = np.random.random((2, 3)).astype("float32")
        output_np = np.copy(ref_np)
        output_np[index_np] = updates_np
        self.inputs = {"X": ref_np, "Ids": index_np, "Updates": updates_np}
        self.outputs = {"Out": output_np}

    def test_check_output(self):
        self.check_output_with_place(self.place, check_eager=False)

    def test_check_grad(self):
        self.check_grad(["X", "Updates"], "Out", check_eager=False)


class TestScatterOpFp16(OpTest):
    def setUp(self):
        self.op_type = "scatter"
        self.place = paddle.CustomPlace("mlu", 0)
        self.__class__.use_custom_device = True
        self.python_api = paddle.scatter
        ref_np = np.ones((3, 3)).astype("float16")
        index_np = np.array([1, 2]).astype("int32")
        updates_np = np.random.random((2, 3)).astype("float16")
        output_np = np.copy(ref_np)
        output_np[index_np] = updates_np
        self.inputs = {"X": ref_np, "Ids": index_np, "Updates": updates_np}
        self.attrs = {"overwrite": True}
        self.outputs = {"Out": output_np}

    def test_check_output(self):
        self.check_output_with_place(self.place, check_eager=False)

    def test_check_grad(self):
        self.check_grad(["X", "Updates"], "Out", check_eager=False)


if __name__ == "__main__":
    unittest.main()
