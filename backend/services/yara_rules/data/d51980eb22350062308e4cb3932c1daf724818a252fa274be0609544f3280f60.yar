rule auto_rule_20250726235013_3264 {
  strings:
    $o0 = "fnCallback" wide ascii nocase
    $o1 = "dword_46D3C0" wide ascii nocase
  condition:
    all of them
}