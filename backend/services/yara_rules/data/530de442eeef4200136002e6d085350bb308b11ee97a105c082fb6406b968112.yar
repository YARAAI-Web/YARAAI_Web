rule auto_rule_20250727033256_5804 {
  strings:
    $o0 = "dword_47680C" wide ascii nocase
    $o1 = "GetLocaleInfoA" wide ascii nocase
  condition:
    all of them
}