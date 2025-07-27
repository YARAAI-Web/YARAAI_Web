rule auto_rule_20250726212541_7245 {
  strings:
    $o0 = "dword_47F38C" wide ascii nocase
    $o1 = "_set_exp" wide ascii nocase
  condition:
    all of them
}