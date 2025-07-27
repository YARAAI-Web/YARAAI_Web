rule auto_rule_20250727001714_2133 {
  strings:
    $o0 = "dword_1800141F0" wide ascii nocase
    $o1 = "execute_onexit_table" wide ascii nocase
  condition:
    all of them
}