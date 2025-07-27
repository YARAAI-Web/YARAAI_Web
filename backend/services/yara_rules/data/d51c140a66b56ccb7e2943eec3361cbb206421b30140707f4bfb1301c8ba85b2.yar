rule auto_rule_20250727001522_0415 {
  strings:
    $o0 = "x81084E" wide ascii nocase
    $o1 = "x6960u" wide ascii nocase
    $o2 = "dword_417545" wide ascii nocase
    $o3 = "x3D58u" wide ascii nocase
  condition:
    4 of ($o*)
}