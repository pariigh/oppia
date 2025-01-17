# coding: utf-8
#
# Copyright 2014 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for the config property registry."""

from __future__ import annotations

from core.tests import test_utils


class ConfigPropertyChangeTests(test_utils.GenericTestBase):

    # At Oppia, we require all files to have an associated test file, since
    # that's how the backend test coverage checks detect that there are Python
    # files to cover in the first place. For files that don't have logic
    # (like core/domain/config_domain.py), a trivial test like the one
    # here is sufficient.
    def test_trivial(self) -> None:
        pass
