rule auto_rule_20250727034429_2004 {
  strings:
    $o0 = "dword_46A0B0" wide ascii nocase
    $o1 = "nLine" wide ascii nocase
  condition:
    all of them
}