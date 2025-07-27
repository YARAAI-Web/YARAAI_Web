rule auto_rule_20250726165613_6319 {
  strings:
    $o0 = "F28h" wide ascii nocase
    $o1 = "byte_640291F8" wide ascii nocase
  condition:
    all of them
}