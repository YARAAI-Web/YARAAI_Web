rule auto_rule_20250726141119_9006 {
  strings:
    $o0 = "dword_40B860" wide ascii nocase
    $o1 = "lfHeight" wide ascii nocase
  condition:
    all of them
}