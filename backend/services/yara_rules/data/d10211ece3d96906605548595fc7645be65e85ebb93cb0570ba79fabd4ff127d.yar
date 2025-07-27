rule auto_rule_20250727015635_1468 {
  strings:
    $o0 = "GdipGetImageEncoders" wide ascii nocase
    $o1 = "NtCreateThreadEx" wide ascii nocase
  condition:
    all of them
}