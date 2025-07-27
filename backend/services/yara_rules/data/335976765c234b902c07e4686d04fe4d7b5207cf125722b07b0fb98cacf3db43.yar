rule auto_rule_20250727013113_0439 {
  strings:
    $o0 = "xFF000000" wide ascii nocase
    $o1 = "dword_47667C" wide ascii nocase
  condition:
    all of them
}