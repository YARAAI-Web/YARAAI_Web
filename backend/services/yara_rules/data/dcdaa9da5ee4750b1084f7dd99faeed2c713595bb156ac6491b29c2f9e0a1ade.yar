rule auto_rule_20250726222114_1148 {
  strings:
    $o0 = "CtrlType" wide ascii nocase
    $o1 = "PyObject_CallFunctionObjArgs" wide ascii nocase
  condition:
    all of them
}