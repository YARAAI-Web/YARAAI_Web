rule auto_rule_20250726153457_2636 {
  strings:
    $o0 = "xC38u" wide ascii nocase
    $o1 = "dword_4335B3" wide ascii nocase
  condition:
    all of them
}