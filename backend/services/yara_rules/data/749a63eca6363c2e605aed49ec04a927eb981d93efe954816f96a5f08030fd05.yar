rule auto_rule_20250726095842_6626 {
  strings:
    $o0 = "byte_46FAD6" wide ascii nocase
    $o1 = "dword_46FABC" wide ascii nocase
  condition:
    all of them
}