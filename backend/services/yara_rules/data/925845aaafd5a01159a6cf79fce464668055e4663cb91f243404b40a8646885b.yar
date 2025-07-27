rule auto_rule_20250727032232_8527 {
  strings:
    $o0 = "x476D" wide ascii nocase
    $o1 = "dword_413BB8" wide ascii nocase
  condition:
    all of them
}