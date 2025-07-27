rule auto_rule_20250726225920_5119 {
  strings:
    $o0 = "CopyUnwindUp_0" wide ascii nocase
    $o1 = "dword_443450" wide ascii nocase
  condition:
    all of them
}