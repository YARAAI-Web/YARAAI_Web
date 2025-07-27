rule auto_rule_20250727012543_8606 {
  strings:
    $o0 = "byte_476C5C" wide ascii nocase
    $o1 = "dword_47706C" wide ascii nocase
  condition:
    all of them
}