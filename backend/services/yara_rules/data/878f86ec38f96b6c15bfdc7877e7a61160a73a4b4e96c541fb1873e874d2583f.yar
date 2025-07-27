rule auto_rule_20250726111941_8193 {
  strings:
    $o0 = "dword_6402E98C" wide ascii nocase
  condition:
    all of them
}