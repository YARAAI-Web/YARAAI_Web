rule auto_rule_20250726182301_6143 {
  strings:
    $o0 = "dword_467B94" wide ascii nocase
    $o1 = "_wincmdln" wide ascii nocase
  condition:
    all of them
}