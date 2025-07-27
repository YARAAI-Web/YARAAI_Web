rule auto_rule_20250726144158_3201 {
  strings:
    $o0 = "normal" wide ascii nocase
    $o1 = "dword_464434" wide ascii nocase
  condition:
    all of them
}