rule auto_rule_20250726202659_8981 {
  strings:
    $o0 = "dword_1040706C" wide ascii nocase
  condition:
    all of them
}