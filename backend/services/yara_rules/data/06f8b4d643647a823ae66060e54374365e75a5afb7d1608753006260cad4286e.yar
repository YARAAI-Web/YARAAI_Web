rule auto_rule_20250726131912_4399 {
  strings:
    $o0 = "InterlockedIncrement" wide ascii nocase
    $o1 = "dword_40A2AC" wide ascii nocase
  condition:
    all of them
}