rule auto_rule_20250726060104_1535 {
  strings:
    $o0 = "dword_650303F4" wide ascii nocase
    $o1 = "j__free" wide ascii nocase
  condition:
    all of them
}