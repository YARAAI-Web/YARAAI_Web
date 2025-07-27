rule auto_rule_20250726075354_3792 {
  strings:
    $o0 = "off_402514" wide ascii nocase
    $o1 = "dword_40BB84" wide ascii nocase
  condition:
    all of them
}