rule auto_rule_20250726170530_1691 {
  strings:
    $o0 = "_std_exception_copy" wide ascii nocase
    $o1 = "qword_14008C3D0" wide ascii nocase
  condition:
    all of them
}