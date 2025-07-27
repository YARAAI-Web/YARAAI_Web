rule auto_rule_20250726072657_6149 {
  strings:
    $o0 = "_fltout" wide ascii nocase
    $o1 = "x3FFFu" wide ascii nocase
    $o2 = "dword_40B000" wide ascii nocase
  condition:
    3 of ($o*)
}