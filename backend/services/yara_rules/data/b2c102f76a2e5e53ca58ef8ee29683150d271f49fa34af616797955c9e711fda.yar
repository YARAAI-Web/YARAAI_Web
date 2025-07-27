rule auto_rule_20250726172537_4453 {
  strings:
    $o0 = "xEFu" wide ascii nocase
    $o1 = "RegisterWindowMessageW" wide ascii nocase
    $o2 = "dword_4C1168" wide ascii nocase
  condition:
    3 of ($o*)
}