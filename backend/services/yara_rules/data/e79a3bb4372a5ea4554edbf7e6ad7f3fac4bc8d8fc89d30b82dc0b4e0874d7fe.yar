rule auto_rule_20250726233551_4748 {
  strings:
    $o0 = "dword_78144" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}