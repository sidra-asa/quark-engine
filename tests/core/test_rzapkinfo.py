import pytest
import requests

from quark.core.apkinfo import AndroguardImp
from quark.core.interface.baseapkinfo import BaseApkinfo
from quark.core.rzapkinfo import RizinImp
from quark.core.struct.bytecodeobject import BytecodeObject
from quark.core.struct.methodobject import MethodObject


OPS = [
    {
        "mnemonic": "const-class",
        "parameter": "Landroid/view/KeyEvent;",
        "expect_type": str,
    },
    {
        "mnemonic": "const-wide/16",
        "parameter": 0x3e8,
        "expect_type": float,
    },
    {
        "mnemonic": "invoke-virtual",
        "parameter": ("Ljava/lang/StringBuilder;->append(Ljava/lang/String;)"
                      "Ljava/lang/StringBuilder;"),
        "expect_type": str,
    },
    {
        "mnemonic": "const-string",
        "parameter": "str.google.c.a.tc",
        "expect_type": str,
    },
]


class TestRzApkinfo:

    def test_parse_parameter(self):
        for op in OPS:
            parsed_param = RizinImp._parse_parameter(op.get("parameter"))
            assert isinstance(parsed_param, op.get("expect_type"))
