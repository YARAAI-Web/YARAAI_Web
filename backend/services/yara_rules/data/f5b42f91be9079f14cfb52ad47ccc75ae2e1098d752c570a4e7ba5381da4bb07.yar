rule auto_rule_20250727005735_5698 {
  strings:
    $o0 = "dword_41D964" wide ascii nocase
    $o1 = "hdcb" wide ascii nocase
  condition:
    all of them
}