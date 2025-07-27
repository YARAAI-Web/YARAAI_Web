rule auto_rule_20250726165206_9019 {
  strings:
    $o0 = "PyObject_Str" wide ascii nocase
    $o1 = "qword_140043DC8" wide ascii nocase
  condition:
    all of them
}