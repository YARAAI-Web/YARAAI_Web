rule auto_rule_20250726110001_8476 {
  strings:
    $o0 = "off_42753C" wide ascii nocase
    $o1 = "dword_4281F0" wide ascii nocase
  condition:
    all of them
}