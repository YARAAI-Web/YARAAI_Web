rule auto_rule_20250726230500_4127 {
  strings:
    $o0 = "dword_46908C" wide ascii nocase
    $o1 = "_itoa" wide ascii nocase
  condition:
    all of them
}