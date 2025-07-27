rule auto_rule_20250727015530_0606 {
  strings:
    $o0 = "ExpandEnvStrings" wide ascii nocase
    $o1 = "dword_4C1284" wide ascii nocase
  condition:
    all of them
}